from fastapi import FastAPI, HTTPException
from .routes import auth_routes, auth, config, database, models, schemas
from fastapi.responses import HTMLResponse
from fastapi.staticfiles import StaticFiles
from pathlib import Path
from fastapi.templating import Jinja2Templates
from fastapi.requests import Request
import os
from pydantic import BaseModel
import uuid
from motor.motor_asyncio import AsyncIOMotorClient
from config import Config
from typing import List, Optional

# MongoDB Client initialization
client = AsyncIOMotorClient(Config.MONGODB_URI)
db = client[Config.DB_NAME]

# Pydantic model for the data we will receive
class SaveListRequest(BaseModel):
    selectedItems: List[str]
    responseCode: str
    listName: str

class SavedListResponse(BaseModel):
    listName: str
    selectedItems: List[str]
    responseCode: str

app = FastAPI()

# Register router
app.include_router(auth_routes.router, prefix="/auth", tags=["Authentication"])


# Serve static files (app.js, style.css)
app.mount("/static", StaticFiles(directory="app/static"), name="static")

# Path to templates directory
templates_path = os.path.join(os.getcwd(), "app", "templates")
templates = Jinja2Templates(directory=templates_path)

@app.get("/", response_class=HTMLResponse)
async def get_home(request: Request):
    return templates.TemplateResponse("home.html", {"request": request})


@app.get("/dashboard", response_class=HTMLResponse)
async def get_dashboard(request: Request):
    return templates.TemplateResponse("dashboard.html", {"request": request})



@app.get("/search")
async def search(code: str):
    """
    Searches for HTTP dog images based on the status code or pattern (e.g., 2xx).
    """
    base_url = "https://http.dog"
    try:
        if len(code) == 1:  # Match all "x00"
            possible_codes = [f"{code}{i}{j}" for i in range(10) for j in range(10)]
        elif len(code) == 2:  # Match all "xx0"
            possible_codes = [f"{code}{i}" for i in range(10)]
        elif len(code) == 3:  # Match exactly
            possible_codes = [code]
        else:
            raise HTTPException(status_code=400, detail="Invalid status code format.")

        results = [
            f"{base_url}/{status}.jpg"
            for status in possible_codes
            if 100 <= int(status) < 1000
        ]

        if not results:
            raise HTTPException(status_code=404, detail="No images found for the code.")

        return {"images": results}
    except ValueError:
        raise HTTPException(status_code=400, detail="Invalid status code format.")


@app.post("/save", response_model=SavedListResponse)
async def save_list(data: SaveListRequest):
    collection = db["saved_lists"]
    saved_data = {
        "listName": data.listName,
        "selectedItems": data.selectedItems,
        "responseCode": data.responseCode
    }

    # Insert the data into MongoDB
    result = await collection.insert_one(saved_data)

    if result.acknowledged:
        return saved_data
    else:
        raise HTTPException(status_code=500, detail="Failed to save data")

# Get route to fetch all saved lists
@app.get("/lists", response_model=List[SavedListResponse])
async def get_saved_lists():
    collection = db["saved_lists"]
    saved_lists = await collection.find().to_list(length=100)  # Fetch up to 100 lists
    return saved_lists

# Delete route to remove a saved list by listName
@app.delete("/lists/{listName}")
async def delete_list(listName: str):
    collection = db["saved_lists"]
    result = await collection.delete_one({"listName": listName})
    if result.deleted_count == 0:
        raise HTTPException(status_code=404, detail="List not found")
    return {"message": "List deleted successfully"}

    
@app.put("/lists/{listName}")
async def edit_list(listName: str, list: SavedListResponse):
    collection = db["saved_lists"]
    result = await collection.update_one(
        {"listName": listName}, 
        {"$set": {"listName": list.listName, "responseCode": list.responseCode, "images": list.images}}
    )
    if result.matched_count == 0:
        raise HTTPException(status_code=404, detail="List not found")
    return {"message": "List updated successfully"}

