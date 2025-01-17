const formOpenBtn = document.querySelector("#form-open"),
  home = document.querySelector(".home"),
  formContainer = document.querySelector(".form_container"),
  formCloseBtn = document.querySelector(".form_close"),
  signupBtn = document.querySelector("#signup"),
  loginBtn = document.querySelector("#login"),
  pwShowHide = document.querySelectorAll(".pw_hide");

// Open form on button click
formOpenBtn.addEventListener("click", () => {
  home.classList.add("show");
});

// Close form on close button click
formCloseBtn.addEventListener("click", () => {
  home.classList.remove("show");
});

// Toggle password visibility
pwShowHide.forEach((icon) => {
  icon.addEventListener("click", () => {
    const pwInput = icon.parentElement.querySelector("input");
    if (pwInput.type === "password") {
      pwInput.type = "text";
      icon.classList.replace("uil-eye-slash", "uil-eye");
    } else {
      pwInput.type = "password";
      icon.classList.replace("uil-eye", "uil-eye-slash");
    }
  });
});

// Toggle between signup and login forms
signupBtn.addEventListener("click", (e) => {
  e.preventDefault();
  formContainer.classList.add("active"); // Show signup form
});

loginBtn.addEventListener("click", (e) => {
  e.preventDefault();
  formContainer.classList.remove("active"); // Show login form
});

// Signup Form Submission
document.getElementById("signupForm").addEventListener("submit", async function (e) {
  e.preventDefault();

  // Capture form data
  const username = document.getElementById("username").value;
  const email = document.getElementById("signup_email").value;
  const mobile = document.getElementById("mobile").value;
  const password = document.getElementById("signup_password").value;
  const confirmPassword = document.getElementById("confirm_password").value;

  // Validate password match
  if (password !== confirmPassword) {
    Swal.fire("Error", "Passwords do not match", "error");
    return;
  }

  // Prepare the data to send to the backend
  const userData = { username, email, mobile, password };

  // Send data to the backend API
  try {
    const response = await fetch("http://127.0.0.1:8000/auth/register", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(userData),
    });

    const result = await response.json();
    if (response.ok) {
      Swal.fire("Success", result.message, "success").then(() => {
        formContainer.classList.remove("active"); // Show login form
      });
    } else {
      Swal.fire("Registration Failed", result.detail || "An error occurred", "error");
    }
  } catch (error) {
    console.error("Error:", error);
    Swal.fire("Error", "An error occurred while registering", "error");
  }
});

// Login Form Submission
document.getElementById("loginForm").addEventListener("submit", async function (e) {
  e.preventDefault(); // Prevent default form submission

  // Capture form data
  const email = document.getElementById("login_email").value;
  const password = document.getElementById("login_password").value;

  // Prepare the data to send to the backend
  const loginData = { email, password };

  // Send data to the backend API
  try {
    const response = await fetch("http://127.0.0.1:8000/auth/login", {
      method: "POST",
      headers: { "Content-Type": "application/json" },
      body: JSON.stringify(loginData),
    });

    const result = await response.json();
    if (response.ok) {
      Swal.fire("Success", result.message, "success").then(() => {
        localStorage.setItem("access_token", result.access_token); // Store JWT token
        window.location.href = "/dashboard"; // Redirect on successful login
      });
    } else {
      Swal.fire("Login Failed", result.detail || "An error occurred", "error");
    }
  } catch (error) {
    console.error("Error:", error);
    Swal.fire("Error", "An error occurred while logging in", "error");
  }
});



