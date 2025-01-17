# HTTP Dog Images Project 🐶

## Overview 🌟

Welcome to the **HTTP Dog Images** project! This web-based application lets users search for dog images based on HTTP status codes and save their favorite images to custom lists. The application also offers functionality for filtering images by response code, creating lists, and managing them through an intuitive interface. Whether you’re learning about HTTP codes or just love dogs, this app is designed to be both fun and educational!

### Key Features:
- **Search Dog Images** based on HTTP response codes (e.g., `200`, `404`, `2xx`).
- **Save Custom Lists** of images based on selected HTTP codes.
- **View and Manage Lists** with options to edit or delete saved lists.
- **Responsive Design** ensuring smooth usability across all devices.

The project is built using **FastAPI**, **HTML**, **CSS**, **JavaScript**, and **Bootstrap**, providing a modern and clean user interface.

---

## Technologies Used ⚙️

- **Backend**: [FastAPI](https://fastapi.tiangolo.com/) (Python)
- **Frontend**: **HTML**, **CSS**, **JavaScript**
- **Styling**: [Bootstrap 5](https://getbootstrap.com/) for responsive, mobile-first design
- **API**: Custom API for fetching dog images based on HTTP response codes from [http.dog](https://http.dog/)
- **Database**: MongoDB to store user login data, lists, and image links
- **JavaScript**: Dynamic user interactions, API calls, and image filtering
- **CSS**: Custom styles and animations for a polished look

---

## Pages and Functionality 🖥️

### 1. **Login/Signup Page** 🔐
- **Description**: Users can create an account or log in to access their custom lists and saved images. Authentication ensures that each user can manage their own lists.
- **Features**: Login, Sign Up, Error handling for invalid credentials.

### 2. **Search Page** 🔍
- **Description**: On this page, users can filter dog images by HTTP response code (e.g., `203`, `2xx`, `3xx`). Each filter will display corresponding dog images, and users can select which images they want to save.
- **Features**:
  - Filter by individual HTTP codes like `203`, `2xx`, `3xx`, etc.
  - Show images matching the filtered response codes.
  - Option to save filtered images into custom lists.

### 3. **Lists Page** 🗂️
- **Description**: Users can view, edit, and delete their saved lists. This page displays all lists, allowing users to see the images stored under each list and manage them.
- **Features**:
  - View saved lists with details like list name, response codes, and image links.
  - Edit existing lists (modify images or name).
  - Delete lists.

---

## Key Features and Implementation Details 🎯

### 1. **Search and Filter Functionality** 🔍
- **Description**: The app allows users to filter dog images by specific HTTP response codes. For example:
  - Filter by `203` to display only dog images related to the `203` response code.
  - Filter by `2xx` to show all dog images corresponding to HTTP codes starting with `2`.
  - Similarly, you can filter by `20x`, `3xx`, and other codes.
  
- **How it Works**:
  - When a user selects a filter (like `2xx`), the app fetches images based on that filter.
  - Once the images are displayed, users can select the images they like and save them into a custom list.

### 2. **Save Custom Lists** 💾
- **Description**: Users can save their filtered images into named lists for future access. Each list will store the images related to a specific HTTP response code, along with the creation date, code details, and image links.
  
- **How it Works**:
  - After applying a filter, users can save their selected dog images into a list. They will be prompted to name the list before saving.
  - Each list will include the images corresponding to the response codes shown during the search.

### 3. **Manage Lists** 🗂️
- **Description**: On the Lists page, users can view all their saved lists, and they will have the option to edit or delete any list they’ve created.
  
- **How it Works**:
  - Users can select a list to view the dog images associated with it.
  - Lists can be edited or deleted directly from this page, giving users full control over their saved content.

### 4. **Editing Lists** ✏️
- **Description**: Users can edit their saved lists to add or remove images and change the list name.
  
- **How it Works**:
  - When editing a list, users can modify the selected dog images or rename the list.
  - Users can also add new dog images by filtering and selecting new images.

### 5. **Responsive Design** 📱💻
- **Description**: The application uses **Bootstrap 5** to ensure it’s fully responsive, adapting seamlessly to different screen sizes from mobile phones to large desktop monitors.
  
- **How it Works**:
  - The layout adjusts based on the user’s screen size, ensuring a smooth and consistent experience across all devices.

---
# HTTP_request_code
