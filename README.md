# Secure_Nigeria
ALX BE Capstone
# Nigeria Security Awareness API 🇳🇬

**"Security is everyone's business."**

Welcome to the **Nigeria Security Awareness API**, my capstone project. In a country where security information is often scattered or unverified, I built this system to bridge the gap. It allows real-time incident reporting, community verification, and easy access to emergency help.

This isn't just a database; it's a tool to empower citizens with the information they need to stay safe.

## 🚀 Live Demo
**Base URL:** `https://secure-nigeria.onrender.com`
*(Note: This is a backend API. You can test these endpoints using Postman.)*

---

## 💡 What Can You Do With It?

* **📍 Report Incidents:** Witnessed something? Log it immediately with specific location details (State, LGA, Address).
* **📢 Stay Informed:** View a "Feed" of security alerts happening around you, from robberies to accidents.
* **🚓 Find Help Fast:** I have pre-loaded a database of **802 Emergency Stations** (Police, Fire, Military, Hospitals) across Nigeria.
* **🔔 Get Notified:** Follow other users and get automatic notifications when they post updates.
* **✅ Trust but Verify:** Fight fake news by "Verifying" or disputing reports.

---

## 🛠️ Tech Stack
I chose **Django** for its robustness and security features—essential for a platform handling sensitive data.

* **Backend:** Python, Django REST Framework (DRF)
* **Database:** PostgreSQL (Production), SQLite (Development)
* **Hosting:** Deployed live on Render
* **Key Libraries:** `django-filter` (Filtering), `cloudinary` (Image Hosting).

---

## ⚡ Quick Start (Run it locally)

1.  **Clone the repo:**
    ```bash
    git clone https://github.com/OlayinkaAdebisi/Secure_Nigeria.git
    ```

2.  **Install dependencies:**
    ```bash
    pip install -r requirements.txt
    ```

3.  **Set up secrets:**
    Create a `.env` file and add your keys:
    ```
    SECRET_KEY=your_key_here
    DEBUG=True
    ```

4.  **Run the server:**
    ```bash
    python manage.py runserver
    ```

---

## 📚 API Documentation & Test Data

Here is exactly how to test the system in Postman.

### 1️⃣ User Accounts (Authentication)
*Everything starts here. You need a token to do anything else.*

| Method | Endpoint | Description |
| :--- | :--- | :--- |
| **POST** | `/secure_nigeria/signup/` | Create a new account |
| **POST** | `/secure_nigeria/login/` | **Login (Get Token)** |
| **POST** | `/secure_nigeria/follow/<id>/` | Follow another user |
| **POST** | `/secure_nigeria/unfollow/<id>/` | Unfollow another user |

**📝 JSON Body for Sign Up:**
```json
{
    "username": "naija_security_admin",
    "email": "admin@secure.ng",
    "password": "SecurePassword123!",
    "phone_number": "08012345678",
    "first_name": "Adebisi",
    "last_name": "Olayinka"
}
