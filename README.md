# 🌍 WorldInfo

### Country Information • Comparison • Weather • Currency

WorldInfo is a Python Flask web application designed to provide useful information about countries through a simple and user-friendly web interface.

The project combines a **Python Flask backend**, **SQLite database**, and **external APIs** to provide country information, weather data, and currency conversion.

---

## 🚀 Live Demo

👉 https://yatharthkale.pythonanywhere.com/

---

## 🎯 Project Objective

The main objective of WorldInfo is to create a simple platform where users can:

- Explore country information
- Search for countries
- Compare countries
- Convert currencies
- Check weather information
- Retrieve information through API endpoints

The project also demonstrates how a Python backend can communicate with a database and external APIs.

---

# ✨ Features

- 🌍 Country information
- 🔎 Country search
- ⚖️ Country comparison
- 🌦️ Weather information
- 💱 Currency conversion
- 🎲 Random country
- 📊 JSON API endpoints
- 🗄️ SQLite database
- ☁️ Cloud deployment
- 🔌 REST-style backend endpoints

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework and backend API |
| SQLite | Database |
| HTML | Website structure |
| CSS | Website styling |
| REST APIs | External/live data |
| JSON | Data exchange |
| Python Requests | API communication |
| PythonAnywhere | Cloud deployment |

---

# 🏗️ System Architecture

```text
                         USER
                           │
                           ▼
                     WEB BROWSER
                           │
                           ▼
                  ┌─────────────────┐
                  │   FLASK APP     │
                  │     PYTHON      │
                  └────────┬────────┘
                           │
              ┌────────────┼────────────┐
              │            │            │
              ▼            ▼            ▼
        ┌──────────┐  ┌──────────┐  ┌────────────┐
        │  SQLite  │  │ Currency │  │  Weather   │
        │ Database │  │   API    │  │    API     │
        └────┬─────┘  └────┬─────┘  └─────┬──────┘
             │              │              │
             ▼              ▼              ▼
        Country Data    Exchange Rates   Open-Meteo
🔧 Backend

The backend of WorldInfo is developed using Python and Flask.

The main backend file is:

worldinfo_api.py

Flask handles:

Website routes
API routes
Database operations
External API requests
Data processing
JSON responses
🗄️ Database

WorldInfo uses SQLite as its database.

Database file:

worldinfo.db

SQLite is used to store structured application data such as country information and application/search data.

The Python backend communicates with the SQLite database using Python's sqlite3 module.

Database Flow
User Request
     ↓
Flask Backend
     ↓
SQLite Database
     ↓
Country Record
     ↓
JSON / Website Response
🌦️ Weather API

WorldInfo uses the Open-Meteo API for weather information.

The backend sends a request to the external weather service and processes the response before displaying it on the website.

Example API
/api/weather/India
Live API Proof

https://yatharthkale.pythonanywhere.com/api/weather/India

The response is returned in JSON format.

Example structure:

{
    "success": true,
    "source": "Open-Meteo API",
    "country": "India",
    "weather": {}
}
💱 Currency Conversion API

WorldInfo uses an external exchange-rate service for currency conversion.

The backend also has a fallback service in case the primary service is unavailable.

Example
/api/convert?from=USD&to=INR&amount=100
Live API Proof

https://yatharthkale.pythonanywhere.com/api/convert?from=USD&to=INR&amount=100

The result is returned as JSON.

Example:

{
    "result": 9484.3169,
    "source": "open.er-api.com (Frankfurter fallback)"
}

The actual exchange result can change because exchange rates are external data.

🌍 Country API

WorldInfo provides country information through its own Flask backend.

Example
/api/country/India
Live API Proof

https://yatharthkale.pythonanywhere.com/api/country/India

The Flask backend retrieves the country information from the application's SQLite database and returns it as JSON.

📋 Countries API

The application also provides an endpoint for retrieving country records.

Endpoint
/api/countries
Live API Proof

https://yatharthkale.pythonanywhere.com/api/countries

❤️ Backend Health Check

WorldInfo includes a health-check endpoint to verify that the backend is running.

Endpoint
/health
Live Proof

https://yatharthkale.pythonanywhere.com/health

🔌 API Endpoints
Endpoint	Purpose
/api/country/India	Get country information
/api/countries	Get country records
/api/weather/India	Get weather information
/api/convert	Convert currencies
/api/history	Get search history
/api/random	Get a random country
/health	Check backend status
🔄 Data Flow
Country Information
User
 ↓
Website
 ↓
Flask Backend
 ↓
SQLite Database
 ↓
Country Information
 ↓
Website
Weather
User
 ↓
Website
 ↓
Flask Backend
 ↓
Open-Meteo API
 ↓
Weather Data
 ↓
Website
Currency
User
 ↓
Website
 ↓
Flask Backend
 ↓
Exchange Rate API
 ↓
Conversion Result
 ↓
Website
📁 Project Structure
WorldInfo/
│
├── worldinfo_api.py
├── requirements.txt
└── README.md

The SQLite database is used by the deployed application.

📦 Requirements

The project requires Python packages listed in:

requirements.txt

Main dependencies include:

Flask
requests
☁️ Deployment

WorldInfo is deployed using PythonAnywhere.

The Flask application is connected to the PythonAnywhere web server using a WSGI configuration.

Deployment flow:

GitHub
   ↓
Python Flask Application
   ↓
PythonAnywhere
   ↓
Web Server
   ↓
Live Website
🔍 Backend Proof

The backend can be demonstrated through the following:

1. Python Backend
worldinfo_api.py

Contains the Flask application, routes, database operations and API communication.

2. Database
worldinfo.db

SQLite database used by the application.

3. Weather API
/api/weather/India

Returns weather data through the Flask backend.

4. Currency API
/api/convert?from=USD&to=INR&amount=100

Returns currency conversion data.

5. Country API
/api/country/India

Returns country information from the application's database.

6. Health Check
/health

Confirms that the backend application is running.

🎓 Project Demonstration

During the project demonstration, the following can be shown:

Open the live WorldInfo website.
Demonstrate country search and information.
Demonstrate country comparison.
Demonstrate currency conversion.
Demonstrate weather information.
Open the API endpoints and show their JSON responses.
Open worldinfo_api.py and explain the Flask backend.
Show worldinfo.db and explain the database.
Show the WSGI configuration on PythonAnywhere.
Show the live deployed website.

This demonstrates the complete flow from the frontend to the backend, database, external APIs and cloud deployment.

🔮 Future Scope

Possible future improvements include:

More countries and detailed datasets
More live APIs
More comparison categories
Improved caching
User accounts
More advanced analytics
Mobile-friendly improvements
Additional data visualization
👨‍💻 Project Information

Project Name: WorldInfo

Backend: Python Flask

Database: SQLite

Deployment: PythonAnywhere

Data Sources: SQLite database and external APIs

Live Website:
https://yatharthkale.pythonanywhere.com/

📌 Conclusion

WorldInfo demonstrates how a complete web application can be developed using Python Flask, connected to a SQLite database, integrated with external APIs, and deployed on a cloud platform.

The project provides both a user-friendly interface and backend API endpoints that can be directly tested through JSON responses.
