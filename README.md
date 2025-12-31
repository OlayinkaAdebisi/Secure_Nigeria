# Secure Nigeria 🇳🇬

**ALX BE Capstone Project** | Nigeria Security Awareness API

[![Python 100%](https://img.shields.io/badge/Python-100%25-blue?style=flat-square)](https://python.org)
[![Django REST Framework](https://img.shields.io/badge/Django%20REST-Framework-darkgreen?style=flat-square)](https://www.django-rest-framework.org/)
[![Live on Render](https://img.shields.io/badge/Live-Render-46E3B7?style=flat-square)](https://secure-nigeria.onrender.com)

> "Security is everyone's business."

Welcome to the **Nigeria Security Awareness API**, my capstone project for the **ALX Backend Engineering** program. In a country where security information is often scattered or unverified, I built this system to bridge the gap.  It allows real-time incident reporting, community verification, and easy access to emergency help.

This isn't just a database; it's a tool to empower citizens with the information they need to stay safe. 

---

## 🚀 Live Demo

**Base URL:** https://secure-nigeria.onrender.com

> **Note:** This is a backend API.  You can test these endpoints using Postman, cURL, or any HTTP client.

**API Prefix:** `/secure_nigeria/`

---

## 💡 What Can You Do With It

### 📍 Report Incidents Instantly
See something happening? Log it immediately with full details like State, LGA, and exact address.

### 📢 Stay Informed With Live Security Updates
View a real time Feed of alerts around you including robberies, accidents, missing persons, fire outbreaks and more.

### 🚑 Find Help Fast Using Smart Location Technology
I built a **Haversine Coordinate Distance Calculator** into the system.  
It takes your current GPS coordinates and **automatically finds and suggests the nearest emergency station to you**.  
This means you do not need to search manually. The system calculates distance for you and shows the closest help option within seconds.

### 🗂️ Nationwide Coverage (My Dataset)
I manually extracted and compiled **a dataset of 802 police stations across every state in Nigeria** and stored it in JSON format.  
This allows the location feature to work anywhere in the country.

### 🔔 Notification System
Follow other users and receive automatic alerts when they post incident updates.

### 🛑 Fight Misinformation
Verify or dispute reports to keep the platform accurate and trustworthy.


---

## 🛠️ Tech Stack

**Language Composition:** Python 100%

I chose Django for its robustness, security features, and scalability—essential for a platform handling sensitive security data. 

- **Backend Framework:** Python 3.10+ with Django REST Framework (DRF)
- **Database:** PostgreSQL (Production) | SQLite (Development)
- **Hosting:** Deployed on Render (https://secure-nigeria.onrender.com)
- **Key Libraries:**
  - `djangorestframework` — API development
  - `django-filter` — Advanced filtering
  - `cloudinary` — Image hosting
  - `django-cors-headers` — CORS support
  - `python-decouple` — Environment variable management

---

## ⚡ Quick Start (Run it Locally)

### Prerequisites

- Python 3.10+
- pip & virtualenv
- PostgreSQL (optional, SQLite works for development)
- Git

### 1. Clone the repository

```bash
git clone https://github.com/OlayinkaAdebisi/Secure_Nigeria.git
cd Secure_Nigeria
```

### 2. Create and activate virtual environment

```bash
# Create virtual environment
python3 -m venv venv

# Activate it
# On macOS/Linux:
source venv/bin/activate

# On Windows:
venv\Scripts\activate
```

### 3. Install dependencies

```bash
pip install --upgrade pip
pip install -r requirements.txt
```

### 4. Set up environment variables

Create a `.env` file in the project root:

```bash
# Copy example if available
cp .env.example .env

# Edit .env with your values: 
SECRET_KEY=your_django_secret_key_here
DEBUG=True
ALLOWED_HOSTS=localhost,127.0.0.1
DATABASE_URL=sqlite:///db.sqlite3

# For Cloudinary (image hosting)
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret
```

### 5. Run database migrations

```bash
python manage.py migrate
```

### 6. Create a superuser (optional, for admin panel)

```bash
python manage.py createsuperuser
```

### 7. Start the development server

```bash
python manage.py runserver
```

The API will be available at `http://localhost:8000`

Visit the admin panel at `http://localhost:8000/admin/`

---

## 📚 Complete API Endpoints List

### Base URLs
| Environment | URL |
|---|---|
| **Production** | https://secure-nigeria.onrender.com |
| **Local Development** | http://localhost:8000 |
| **API Prefix** | `/secure_nigeria/` |

### Full Endpoint Format
```
https://secure-nigeria.onrender.com/secure_nigeria/{endpoint}
```

### Authentication
All protected endpoints require a Bearer token in the Authorization header: 

```
Authorization: Token <your_access_token>
```

Obtain your token by logging in via the `/secure_nigeria/login/` endpoint.

---
### 🗺️ Complete Endpoint List (Quick Reference)

**Base URL:** https://secure-nigeria.onrender.com  
**Prefix:** `/secure_nigeria/`  
**Full Pattern:** `https://secure-nigeria.onrender.com/secure_nigeria/{endpoint}`

---

#### 🔐 Authentication & Users
- POST `/secure_nigeria/signup/`
- POST `/secure_nigeria/login/`
- GET `/secure_nigeria/profile/`
- PATCH `/secure_nigeria/profile/{id}/`
- POST `/secure_nigeria/follow/{user_id}/`
- POST `/secure_nigeria/unfollow/{user_id}/`

---

#### 📍 Location Reporting
- POST `/secure_nigeria/location/`  
  > ⚡ **Nearest Station Lookup:** When you report a new location, the system automatically runs the **Haversine Distance Calculator** using your coordinates and returns the **closest emergency station** to your reported location.  
- GET `/secure_nigeria/location/`
- GET `/secure_nigeria/location/{id}/`

---

#### 📢 Security Feed
- POST `/secure_nigeria/feed/`
- GET `/secure_nigeria/feed/`
- GET `/secure_nigeria/feed/{id}/`
- PATCH `/secure_nigeria/feed/{id}/`
- POST `/secure_nigeria/feed/verify/{id}/`
- POST `/secure_nigeria/feed/unverify/{id}/`

---

#### 💬 Comments on Feed Posts
- POST `/secure_nigeria/comment/`
- GET `/secure_nigeria/comment/?feed={feed_id}`

---

#### 🚓 Emergency Stations
- GET `/secure_nigeria/stations/` — List all 802+ emergency stations (JSON)  
- GET `/secure_nigeria/stations/{id}/` — Get details of a single station  

> ⚡ **Note:** The nearest station feature is automatically triggered when creating a **location report**, so no separate endpoint is needed.

---

#### ⚠️ High-Risk Areas
- POST `/secure_nigeria/risk/`
- GET `/secure_nigeria/risk/`

---

#### 🔔 Notifications
- GET `/secure_nigeria/notification/`
---
## 🔐 **1. Authentication & User Accounts** (`/secure_nigeria/`)

### Register / Sign Up

| Field | Value |
|-------|-------|
| **URL** | `POST /secure_nigeria/signup/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/signup/` |
| **Authentication** | Not required |
| **Description** | Create a new user account |

**Request Body (JSON):**
```json
{
    "username": "naija_security_admin",
    "email": "admin@secure. ng",
    "password": "SecurePassword123!",
    "phone_number": "08012345678",
    "first_name": "Adebisi",
    "last_name":  "Olayinka"
}
```

**Response (201 Created):**
```json
{
    "id": 1,
    "username": "naija_security_admin",
    "email": "admin@secure. ng",
    "first_name": "Adebisi",
    "last_name": "Olayinka",
    "phone_number": "08012345678",
    "message": "User created successfully"
}
```

---

### Login

| Field | Value |
|-------|-------|
| **URL** | `POST /secure_nigeria/login/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/login/` |
| **Authentication** | Not required |
| **Description** | Authenticate and get access token |

**Request Body (JSON):**
```json
{
    "username": "naija_security_admin",
    "password": "SecurePassword123!"
}
```

**Response (200 OK):**
```json
{
    "token": "eyJ0eXAiOiJKV1QiLCJhbGc.. .",
    "user_id": 1,
    "username": "naija_security_admin",
    "email": "admin@secure.ng",
    "expires_in": 86400
}
```

---

### Get My Profile

| Field | Value |
|-------|-------|
| **URL** | `GET /secure_nigeria/profile/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/profile/` |
| **Authentication** | ✅ Required (Bearer Token) |
| **Description** | Retrieve current user profile |

**Request Headers:**
```
Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGc... 
```

**Response (200 OK):**
```json
{
    "id": 1,
    "username": "naija_security_admin",
    "email": "admin@secure.ng",
    "first_name":  "Adebisi",
    "last_name": "Olayinka",
    "phone_number": "08012345678",
    "date_joined": "2025-12-31T10:00:00Z",
    "followers_count": 5,
    "following_count":  3
}
```

---

### Update My Profile

| Field | Value |
|-------|-------|
| **URL** | `PATCH /secure_nigeria/profile/{id}/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/profile/1/` |
| **Authentication** | ✅ Required (Bearer Token) |
| **Description** | Update user profile information |

**Request Body (JSON):**
```json
{
    "first_name":  "Adebisi",
    "last_name": "Olayinka",
    "phone_number": "08098765432",
    "email": "newemail@secure.ng"
}
```

**Response (200 OK):**
```json
{
    "id":  1,
    "username":  "naija_security_admin",
    "email": "newemail@secure.ng",
    "first_name": "Adebisi",
    "last_name": "Olayinka",
    "phone_number": "08098765432"
}
```

---

### Follow a User

| Field | Value |
|-------|-------|
| **URL** | `POST /secure_nigeria/follow/{user_id}/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/follow/2/` |
| **Authentication** | ✅ Required (Bearer Token) |
| **Description** | Follow another user to get their updates |
| **URL Parameters** | `{user_id}` — ID of user to follow |

**Request Headers:**
```
Authorization: Token eyJ0eXAiOiJKV1QiLCJhbGc...
```

**Response (201 Created):**
```json
{
    "message": "Successfully following user",
    "following_id": 2,
    "following_username": "security_reporter"
}
```

---

### Unfollow a User

| Field | Value |
|-------|-------|
| **URL** | `POST /secure_nigeria/unfollow/{user_id}/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/unfollow/2/` |
| **Authentication** | ✅ Required (Bearer Token) |
| **Description** | Unfollow a user |
| **URL Parameters** | `{user_id}` — ID of user to unfollow |

**Response (200 OK):**
```json
{
    "message":  "Successfully unfollowed user"
}
```

---

## 📍 **2. Location & Incident Reporting** (`/secure_nigeria/`)

### Create Location Report

| Field | Value |
|-------|-------|
| **URL** | `POST /secure_nigeria/location/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/location/` |
| **Authentication** | ✅ Required (Bearer Token) |
| **Description** | Report an incident location (Step 1 of posting alert) |

**Request Body (JSON):**
```json
{
    "latitude": "6.524400",
    "longitude": "3.379200",
    "state": "Lagos",
    "local_government":  "Ikeja",
    "address": "Underbridge, Ikeja",
    "incident_types": "ROBBERY",
    "description": "Armed robbery near the market",
    "report_source": "EYEWITNESS"
}
```

**Allowed Incident Types:**
- `ROBBERY` — Armed/petty robbery
- `TERRORISM` — Terror-related incidents
- `KIDNAPPING` — Abduction cases
- `ACCIDENT` — Road/industrial accidents
- `FIRE` — Fire outbreaks
- `FLOODING` — Flood situations
- `CULTISM` — Cult-related violence
- `OTHER` — Other security incidents

**Response (201 Created):**
```json
{
    "id": 1,
    "latitude": "6.524400",
    "longitude": "3.379200",
    "state": "Lagos",
    "local_government": "Ikeja",
    "address": "Underbridge, Ikeja",
    "incident_types": "ROBBERY",
    "description": "Armed robbery near the market",
    "report_source":  "EYEWITNESS",
    "reported_by": "naija_security_admin",
    "created_at": "2025-12-31T10:30:00Z"
}
```

> ⚠️ **Important:** Save the `id` from the response—you'll need it to create a Feed post! 

---

### List All Locations

| Field | Value |
|-------|-------|
| **URL** | `GET /secure_nigeria/location/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/location/` |
| **Authentication** | Optional |
| **Description** | List all reported incident locations |

**Query Parameters:**
| Parameter | Type | Example | Description |
|-----------|------|---------|-------------|
| `state` | string | `state=Lagos` | Filter by state |
| `incident_types` | string | `incident_types=ROBBERY` | Filter by incident type |
| `page` | integer | `page=1` | Pagination (default: 1) |
| `limit` | integer | `limit=20` | Results per page (default: 20) |

**Example Query:**
```
GET /secure_nigeria/location/?state=Lagos&incident_types=ROBBERY&page=1
```

**Response (200 OK):**
```json
{
    "count": 45,
    "next":  "https://secure-nigeria.onrender.com/secure_nigeria/location/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "latitude": "6.524400",
            "longitude": "3.379200",
            "state": "Lagos",
            "local_government": "Ikeja",
            "address": "Underbridge, Ikeja",
            "incident_types": "ROBBERY",
            "reported_by": "naija_security_admin",
            "created_at": "2025-12-31T10:30:00Z"
        }
    ]
}
```

---

### Get Single Location

| Field | Value |
|-------|-------|
| **URL** | `GET /secure_nigeria/location/{id}/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/location/1/` |
| **Authentication** | Optional |
| **Description** | Get details of a specific location |
| **URL Parameters** | `{id}` — Location ID |

**Response (200 OK):**
```json
{
    "id": 1,
    "latitude": "6.524400",
    "longitude":  "3.379200",
    "state": "Lagos",
    "local_government": "Ikeja",
    "address": "Underbridge, Ikeja",
    "incident_types": "ROBBERY",
    "description": "Armed robbery near the market",
    "report_source": "EYEWITNESS",
    "reported_by": "naija_security_admin",
    "created_at": "2025-12-31T10:30:00Z"
}
```

---

## 📢 **3. Security Feed & Alerts** (`/secure_nigeria/`)

### Create Feed Post (Alert)

| Field | Value |
|-------|-------|
| **URL** | `POST /secure_nigeria/feed/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/feed/` |
| **Authentication** | ✅ Required (Bearer Token) |
| **Description** | Create a security alert (Step 2: After creating location) |

**Request Body (JSON):**
```json
{
    "title": "Robbery Alert - Underbridge",
    "content": "Heavy police presence.  Avoid the underbridge area in Ikeja.  Armed robbery in progress.",
    "location": 1,
    "risk_level": "High"
}
```

**Risk Levels:**
- `High` — Immediate danger
- `Medium` — Caution advised
- `Low` — General awareness

**Response (201 Created):**
```json
{
    "id": 1,
    "title": "Robbery Alert - Underbridge",
    "content": "Heavy police presence. Avoid the underbridge area in Ikeja.",
    "location": 1,
    "risk_level": "High",
    "author": "naija_security_admin",
    "created_at":  "2025-12-31T10:35:00Z",
    "updated_at": "2025-12-31T10:35:00Z",
    "verifications": 0,
    "disputes": 0
}
```

---

### List Feed Posts

| Field | Value |
|-------|-------|
| **URL** | `GET /secure_nigeria/feed/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/feed/` |
| **Authentication** | Optional |
| **Description** | List all security alerts in the feed |

**Query Parameters:**
| Parameter | Type | Example | Description |
|-----------|------|---------|-------------|
| `state` | string | `state=Lagos` | Filter by state |
| `risk_level` | string | `risk_level=High` | Filter by risk level |
| `ordering` | string | `ordering=-created_at` | Sort by field (- for descending) |
| `page` | integer | `page=1` | Pagination |
| `limit` | integer | `limit=20` | Results per page |

**Example Query:**
```
GET /secure_nigeria/feed/?state=Lagos&risk_level=High&ordering=-created_at
```

**Response (200 OK):**
```json
{
    "count": 150,
    "next": "https://secure-nigeria.onrender.com/secure_nigeria/feed/? page=2",
    "previous": null,
    "results":  [
        {
            "id": 1,
            "title": "Robbery Alert - Underbridge",
            "content": "Heavy police presence. Avoid the underbridge area.",
            "location": {
                "id": 1,
                "state": "Lagos",
                "local_government": "Ikeja",
                "address": "Underbridge, Ikeja"
            },
            "risk_level": "High",
            "author": "naija_security_admin",
            "created_at": "2025-12-31T10:35:00Z",
            "verifications": 5,
            "disputes": 0
        }
    ]
}
```

---

### Get Single Feed Post

| Field | Value |
|-------|-------|
| **URL** | `GET /secure_nigeria/feed/{id}/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/feed/1/` |
| **Authentication** | Optional |
| **Description** | Get details of a specific feed post |
| **URL Parameters** | `{id}` — Feed Post ID |

**Response (200 OK):**
```json
{
    "id": 1,
    "title": "Robbery Alert - Underbridge",
    "content": "Heavy police presence.  Avoid the underbridge area.",
    "location": {
        "id": 1,
        "state": "Lagos",
        "local_government": "Ikeja",
        "address": "Underbridge, Ikeja",
        "latitude": "6.524400",
        "longitude":  "3.379200"
    },
    "risk_level":  "High",
    "author":  "naija_security_admin",
    "created_at": "2025-12-31T10:35:00Z",
    "updated_at": "2025-12-31T10:35:00Z",
    "verifications": 5,
    "disputes": 0
}
```

---

### Update Feed Post

| Field | Value |
|-------|-------|
| **URL** | `PATCH /secure_nigeria/feed/{id}/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/feed/1/` |
| **Authentication** | ✅ Required (Bearer Token) |
| **Description** | Update a feed post (owner only) |
| **URL Parameters** | `{id}` — Feed Post ID |

**Request Body (JSON):**
```json
{
    "title": "Robbery Alert - Underbridge [RESOLVED]",
    "content": "Situation now under control. Police have made arrests.",
    "risk_level": "Low"
}
```

**Response (200 OK):**
```json
{
    "id":  1,
    "title":  "Robbery Alert - Underbridge [RESOLVED]",
    "content": "Situation now under control.",
    "risk_level": "Low",
    "updated_at": "2025-12-31T11:00:00Z"
}
```

---

### Verify a Feed Post

| Field | Value |
|-------|-------|
| **URL** | `POST /secure_nigeria/feed/verify/{id}/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/feed/verify/1/` |
| **Authentication** | ✅ Required (Bearer Token) |
| **Description** | Verify that a feed post is accurate/true |
| **URL Parameters** | `{id}` — Feed Post ID |

**Response (201 Created):**
```json
{
    "message": "Post verified successfully",
    "post_id": 1,
    "total_verifications": 6,
    "verified_by": "naija_security_admin"
}
```

---

### Unverify a Feed Post

| Field | Value |
|-------|-------|
| **URL** | `POST /secure_nigeria/feed/unverify/{id}/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/feed/unverify/1/` |
| **Authentication** | ✅ Required (Bearer Token) |
| **Description** | Remove your verification from a post |
| **URL Parameters** | `{id}` — Feed Post ID |

**Response (200 OK):**
```json
{
    "message": "Verification removed successfully",
    "post_id": 1,
    "total_verifications": 5
}
```

---

## 💬 **4. Comments on Feed Posts** (`/secure_nigeria/`)

### Create Comment

| Field | Value |
|-------|-------|
| **URL** | `POST /secure_nigeria/comment/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/comment/` |
| **Authentication** | ✅ Required (Bearer Token) |
| **Description** | Add a comment to a feed post |

**Request Body (JSON):**
```json
{
    "body": "I saw this happening too. Police arrived at 10: 45 AM.",
    "feed":  1
}
```

**Response (201 Created):**
```json
{
    "id": 1,
    "body": "I saw this happening too. Police arrived at 10:45 AM.",
    "feed": 1,
    "author": "naija_security_admin",
    "created_at": "2025-12-31T10:40:00Z"
}
```

---

### List Comments on a Post

| Field | Value |
|-------|-------|
| **URL** | `GET /secure_nigeria/comment/? feed={feed_id}` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/comment/?feed=1` |
| **Authentication** | Optional |
| **Description** | Get all comments on a specific feed post |

**Query Parameters:**
| Parameter | Type | Example |
|-----------|------|---------|
| `feed` | integer | `feed=1` |
| `page` | integer | `page=1` |
| `limit` | integer | `limit=10` |

**Response (200 OK):**
```json
{
    "count":  3,
    "results": [
        {
            "id": 1,
            "body": "I saw this happening too.",
            "feed": 1,
            "author": "naija_security_admin",
            "created_at": "2025-12-31T10:40:00Z"
        }
    ]
}
```

---

## 🚓 **5. Emergency Stations** (`/secure_nigeria/`)

### List All Emergency Stations

| Field | Value |
|-------|-------|
| **URL** | `GET /secure_nigeria/station/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/station/` |
| **Authentication** | Optional |
| **Description** | List all emergency stations (Police, Fire, Military, Hospitals) across Nigeria |
| **Total Records** | 802+ stations pre-loaded |

**Query Parameters:**
| Parameter | Type | Example | Description |
|-----------|------|---------|-------------|
| `state` | string | `state=Lagos` | Filter by state |
| `station_type` | string | `station_type=POLICE` | Filter by type |
| `page` | integer | `page=1` | Pagination |
| `limit` | integer | `limit=20` | Results per page |

**Station Types:**
- `POLICE` — Police stations
- `FIRE` — Fire service stations
- `MILITARY` — Military installations
- `HOSPITAL` — Hospitals & medical centers

**Example Query:**
```
GET /secure_nigeria/station/? state=Lagos&station_type=POLICE
```

**Response (200 OK):**
```json
{
    "count": 802,
    "next": "https://secure-nigeria.onrender.com/secure_nigeria/station/?page=2",
    "previous": null,
    "results": [
        {
            "id": 1,
            "station_name": "Lagos Island Police Station",
            "latitude": "6.5244",
            "longitude": "3.3792",
            "address": "Lagos Island, Lagos",
            "state": "Lagos",
            "station_type": "POLICE",
            "phone": "09012345678"
        },
        {
            "id":  2,
            "station_name": "Lekki Fire Station",
            "latitude": "6.4543",
            "longitude": "3.5789",
            "address": "Lekki, Lagos",
            "state": "Lagos",
            "station_type": "FIRE",
            "phone": "09087654321"
        }
    ]
}
```

---

### Get Single Station

| Field | Value |
|-------|-------|
| **URL** | `GET /secure_nigeria/station/{id}/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/station/1/` |
| **Authentication** | Optional |
| **Description** | Get details of a specific emergency station |

**Response (200 OK):**
```json
{
    "id": 1,
    "station_name": "Lagos Island Police Station",
    "latitude": "6.5244",
    "longitude": "3.3792",
    "address": "Lagos Island, Lagos",
    "state":  "Lagos",
    "station_type": "POLICE",
    "phone": "09012345678"
}
```

---

## ⚠️ **6. High-Risk Areas** (`/secure_nigeria/`)

### Create High-Risk Area Alert

| Field | Value |
|-------|-------|
| **URL** | `POST /secure_nigeria/risk/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/risk/` |
| **Authentication** | ✅ Required (Bearer Token) |
| **Description** | Mark an area as high-risk based on incident patterns |

**Request Body (JSON):**
```json
{
    "location": 1,
    "description": "Multiple terror incidents reported in this area",
    "risk_level": "HIGH",
    "risk_types": "TERRORISM"
}
```

**Risk Levels:**
- `HIGH` — Extreme caution
- `MEDIUM` — Caution advised
- `LOW` — General awareness

**Response (201 Created):**
```json
{
    "id": 1,
    "location": 1,
    "description": "Multiple terror incidents reported",
    "risk_level": "HIGH",
    "risk_types": "TERRORISM",
    "created_by": "naija_security_admin",
    "created_at":  "2025-12-31T10:50:00Z"
}
```

---

### List High-Risk Areas

| Field | Value |
|-------|-------|
| **URL** | `GET /secure_nigeria/risk/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/risk/` |
| **Authentication** | Optional |
| **Description** | List all flagged high-risk areas |

**Query Parameters:**
| Parameter | Type | Example |
|-----------|------|---------|
| `risk_level` | string | `risk_level=HIGH` |
| `state` | string | `state=Kaduna` |
| `page` | integer | `page=1` |

**Response (200 OK):**
```json
{
    "count":  25,
    "results": [
        {
            "id": 1,
            "location": {
                "id": 1,
                "state": "Kaduna",
                "address": "Somwhere"
            },
            "description":  "Multiple terror incidents",
            "risk_level": "HIGH",
            "risk_types": "TERRORISM",
            "created_at": "2025-12-31T10:50:00Z"
        }
    ]
}
```

---

## 🔔 **7. Notifications** (`/secure_nigeria/`)

### Get My Notifications

| Field | Value |
|-------|-------|
| **URL** | `GET /secure_nigeria/notification/` |
| **Full URL** | `https://secure-nigeria.onrender.com/secure_nigeria/notification/` |
| **Authentication** | ✅ Required (Bearer Token) |
| **Description** | Get all notifications (follows, verifications, etc.) |

**Query Parameters:**
| Parameter | Type | Example | Description |
|-----------|------|---------|-------------|
| `read` | boolean | `read=false` | Filter unread notifications |
| `page` | integer | `page=1` | Pagination |
| `limit` | integer | `limit=20` | Results per page |

**Response (200 OK):**
```json
{
    "count": 25,
    "next": "https://secure-nigeria.onrender.com/secure_nigeria/notification/? page=2",
    "previous": null,
    "results":  [
        {
            "id": 1,
            "message": "user123 followed you",
            "notification_type": "FOLLOW",
            "created_at": "2025-12-31T10:15:00Z",
            "read": false
        },
        {
            "id": 2,
            "message": "Your post received a verification",
            "notification_type": "VERIFICATION",
            "created_at": "2025-12-31T09:45:00Z",
            "read": true
        },
        {
            "id":  3,
            "message":  "Someone commented on your post",
            "notification_type": "COMMENT",
            "created_at": "2025-12-31T09:30:00Z",
            "read": true
        }
    ]
}
```

**Notification Types:**
- `FOLLOW` — Someone followed you
- `VERIFICATION` — Your post was verified
- `COMMENT` — Comment on your post
- `ALERT` — Security alert nearby

---

## 📊 Error Codes & Responses

| HTTP Code | Status | Meaning |
|-----------|--------|---------|
| **200** | OK | Request successful |
| **201** | Created | Resource successfully created |
| **204** | No Content | Successful request with no response body |
| **400** | Bad Request | Invalid data or validation error |
| **401** | Unauthorized | Missing or invalid authentication token |
| **403** | Forbidden | Access denied (insufficient permissions) |
| **404** | Not Found | Resource does not exist |
| **422** | Unprocessable Entity | Semantic error in request |
| **500** | Internal Server Error | Server-side error |

**Example Error Response:**
```json
{
    "detail": "Invalid credentials",
    "status_code": 401
}
```

---

## 🧪 Testing with cURL

### Sign Up

```bash
curl -X POST "https://secure-nigeria.onrender.com/secure_nigeria/signup/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "naija_security_admin",
    "email": "admin@secure. ng",
    "password": "SecurePassword123!",
    "phone_number": "08012345678",
    "first_name": "Adebisi",
    "last_name":  "Olayinka"
  }'
```

### Login

```bash
curl -X POST "https://secure-nigeria.onrender.com/secure_nigeria/login/" \
  -H "Content-Type: application/json" \
  -d '{
    "username": "naija_security_admin",
    "password": "SecurePassword123!"
  }'
```

### Get Profile (with token)

```bash
curl -X GET "https://secure-nigeria.onrender.com/secure_nigeria/profile/" \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

### Create Location

```bash
curl -X POST "https://secure-nigeria.onrender.com/secure_nigeria/location/" \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "latitude": "6.524400",
    "longitude": "3.379200",
    "state": "Lagos",
    "local_government": "Ikeja",
    "address": "Underbridge, Ikeja",
    "report_source": "EYEWITNESS",
    "incident_types": "ROBBERY",
    "description":  "Armed robbery near market"
  }'
```

### Create Feed Post

```bash
curl -X POST "https://secure-nigeria.onrender.com/secure_nigeria/feed/" \
  -H "Authorization: Token YOUR_TOKEN_HERE" \
  -H "Content-Type: application/json" \
  -d '{
    "title": "Robbery Alert",
    "content": "Avoid the underbridge.  Heavy police presence.",
    "location": 1,
    "risk_level": "High"
  }'
```

### Verify a Post

```bash
curl -X POST "https://secure-nigeria.onrender.com/secure_nigeria/feed/verify/1/" \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

### List Nearby Stations

```bash
curl -X GET "https://secure-nigeria.onrender.com/secure_nigeria/station/? state=Lagos&station_type=POLICE" \
  -H "Content-Type: application/json"
```

### Get Notifications

```bash
curl -X GET "https://secure-nigeria.onrender.com/secure_nigeria/notification/" \
  -H "Authorization: Token YOUR_TOKEN_HERE"
```

---

## 📖 Postman Collection

Import this as a Postman collection environment:

```json
{
  "client": "Postman",
  "description": "Secure Nigeria API",
  "variables": [
    {
      "key":  "BASE_URL",
      "value":  "https://secure-nigeria.onrender.com"
    },
    {
      "key": "API_PREFIX",
      "value": "/secure_nigeria"
    },
    {
      "key": "TOKEN",
      "value": ""
    }
  ]
}
```

Replace `TOKEN` with your actual bearer token after login.

---

## 🌍 Deployment & Configuration

### Environment Variables (Production)

```bash
# Django settings
SECRET_KEY=your_production_secret_key
DEBUG=False
ALLOWED_HOSTS=secure-nigeria.onrender.com

# Database
DATABASE_URL=postgresql://user:password@hostname: 5432/secure_nigeria_db

# Cloudinary (Image Storage)
CLOUDINARY_CLOUD_NAME=your_cloud_name
CLOUDINARY_API_KEY=your_api_key
CLOUDINARY_API_SECRET=your_api_secret

# CORS
CORS_ALLOWED_ORIGINS=https://your-frontend. com

# Email (optional)
EMAIL_BACKEND=django.core.mail.backends. smtp.EmailBackend
EMAIL_HOST=smtp.gmail.com
EMAIL_PORT=587
EMAIL_USE_TLS=True
EMAIL_HOST_USER=your_email@gmail.com
EMAIL_HOST_PASSWORD=your_app_password
```

### Deploy on Render

1. Push code to GitHub
2. Create new Web Service on Render
3. Connect GitHub repo
4. Set environment variables
5. Deploy

---

## 🤝 Contributing

I welcome contributions!   Here's how you can help:

1. **Fork** the repository
2. **Create a feature branch:**
   ```bash
   git checkout -b feature/amazing-feature
   ```
3. **Make your changes** and test locally
4. **Commit your changes:**
   ```bash
   git commit -m 'Add amazing feature'
   ```
5. **Push to your fork:**
   ```bash
   git push origin feature/amazing-feature
   ```
6. **Open a Pull Request** with a clear description

---

## 🗺️ Roadmap / TODO

- [ ] Add role-based access control (Admin, Moderator, User, Citizen)
- [ ] Implement automated email notifications
- [ ] Add geospatial clustering for incident heatmaps
- [ ] Create mobile app companion (React Native/Flutter)
- [ ] Integrate with official Nigerian emergency services APIs
- [ ] Add real-time WebSocket notifications
- [ ] Implement 2FA for critical operations
- [ ] Add anonymous/pseudonymous reporting option
- [ ] Create admin dashboard with analytics
- [ ] Add multi-language support (Hausa, Yoruba, Igbo)
- [ ] Implement AI-powered incident categorization
- [ ] Add rate limiting and DDoS protection

---

## 📝 License

This project is licensed under the **MIT License**. See the [LICENSE](LICENSE) file for details.

---

## 👤 About the Author

**ADEBISI Olayinka** — ALX Backend Engineering Capstone

I'm a passionate Django/Python developer committed to building technology solutions that address real-world security challenges in Nigeria. This API is my contribution to making communities safer through accessible, verified security information.

- **GitHub:** [@OlayinkaAdebisi](https://github.com/OlayinkaAdebisi)
- **Live API:** https://secure-nigeria.onrender.com
- **Email:** Open an issue on GitHub for inquiries

---

## 🙏 Acknowledgments

- **ALX Backend Engineering Program** for the opportunity and mentorship
- **Django & Django REST Framework** communities
- **Render** for free, reliable hosting
- All testers and contributors

---

<div align="center">

**Made with ❤️ for Nigeria's Security.**

[![Python 100%](https://img.shields.io/badge/Python-100%25-blue?style=flat-square)](https://python.org)
[![Django](https://img.shields.io/badge/Django-REST-darkgreen?style=flat-square&logo=django)](https://www.djangoproject.com/)
[![PostgreSQL](https://img.shields.io/badge/PostgreSQL-Database-336791?style=flat-square&logo=postgresql)](https://www.postgresql.org/)

</div>
