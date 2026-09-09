# 🌍 WorldInfo

WorldInfo is a Python Flask web application that provides useful information about countries, currency conversion, weather information, country comparison, random country selection, and search history.

The project uses a Python Flask backend, SQLite database, external APIs, and is deployed online using PythonAnywhere.

---

## 🔗 Important Links

### 🌐 Live Website
https://yatharthkale.pythonanywhere.com/

### 💻 GitHub Repository
https://github.com/yatharthkale/WorldInfo

### 🐍 Backend Source Code
https://github.com/yatharthkale/WorldInfo/blob/main/worldinfo_api.py

### 📦 Requirements
https://github.com/yatharthkale/WorldInfo/blob/main/requirements.txt

### 🚫 Git Ignore
https://github.com/yatharthkale/WorldInfo/blob/main/.gitignore

---

# 🎯 Project Objective

The main objective of WorldInfo is to provide country-related information through a simple web interface.

The application combines:

- Country information
- Country comparison
- Currency conversion
- Weather information
- Random country selection
- Search history
- REST API endpoints
- SQLite database
- External APIs
- Online deployment

---

# 🛠️ Technology Stack

### Backend
- Python
- Flask
- Requests

### Database
- SQLite

### Frontend
- HTML
- CSS
- JavaScript

### External APIs
- Open-Meteo API
- ExchangeRate API
- Frankfurter API as fallback

### Deployment
- PythonAnywhere

### Version Control
- GitHub

---

# 🏗️ System Architecture

The basic working flow of the application is:

Frontend → Flask Backend → SQLite Database / External APIs → Flask Backend → Frontend

The frontend sends requests to the Flask backend.

The backend processes the request and either:

1. Gets stored information from the SQLite database, or
2. Calls an external API for live information.

The backend then sends the result back to the frontend.

---

# 🐍 Backend

The main backend file is:

`worldinfo_api.py`

GitHub:

https://github.com/yatharthkale/WorldInfo/blob/main/worldinfo_api.py

The backend is developed using Python and Flask.

It handles:

- Application routes
- REST API routes
- Database operations
- Country searches
- Currency conversion
- Weather API requests
- Search history
- Random country selection
- Error handling
- API responses

---

# 🗄️ Database

WorldInfo uses SQLite as its database.

Database file:

`worldinfo.db`

The database is created and used by the application in the same application directory as `worldinfo_api.py`.

On the deployed PythonAnywhere server, the database is used from:

`/home/yatharthkale/worldinfo.db`

The database is not stored in GitHub because database files are excluded using `.gitignore`.

---

# 📊 Database Tables

The SQLite database contains the following main tables.

## 1. countries

Stores country information such as:

- ID
- Country name
- Capital
- Population
- Area
- Continent
- Region
- Currency
- Currency code
- Timezone
- Calling code
- Country code
- Emoji

## 2. currencies

Stores currency information such as:

- Currency code
- Currency name
- Currency symbol

## 3. searches

Stores application search history such as:

- Country searched
- Search time

Indexes are also used for faster searching.

---

# 🔌 Database Connection

The backend connects to SQLite using Python's built-in `sqlite3` module.

The database path is generated using the location of the backend file so that the application can use the database correctly both locally and on the deployed server.

The connection is handled through:

`sqlite3.connect(DB)`

---

# 🌦️ Weather API

WorldInfo uses the Open-Meteo API for weather information.

Official website:

https://open-meteo.com/

API:

https://api.open-meteo.com/v1/forecast

The backend sends latitude and longitude along with weather parameters to Open-Meteo.

The application receives live weather information such as:

- Temperature
- Wind speed
- Weather condition/code

WorldInfo weather API:

https://yatharthkale.pythonanywhere.com/api/weather/India

Source returned by the backend:

`Open-Meteo API`

---

# 💱 Currency Exchange API

WorldInfo uses an exchange-rate API for currency conversion.

Primary API:

https://open.er-api.com/

Main endpoint:

https://open.er-api.com/v6/latest/{base}

Fallback API:

https://api.frankfurter.app/

Fallback endpoint:

https://api.frankfurter.app/latest?from={base}

The backend uses Python's `requests` library to send a request to the exchange-rate API.

The selected base currency is sent to the API and the returned exchange rates are used to calculate the converted amount.

The backend also uses a short cache to reduce unnecessary repeated API requests.

Source returned by the backend:

`open.er-api.com (Frankfurter fallback)`

---

# 🔗 WorldInfo REST API Endpoints

## Country Information

GET:

https://yatharthkale.pythonanywhere.com/api/country/India

Returns country information from the SQLite database.

Source:

`SQLite database: worldinfo.db`

---

## All Countries

GET:

https://yatharthkale.pythonanywhere.com/api/countries

Returns the available countries from the database.

---

## Weather

GET:

https://yatharthkale.pythonanywhere.com/api/weather/India

Returns weather information using Open-Meteo.

Source:

`Open-Meteo API`

---

## Currency Conversion

POST:

`/api/convert`

The currency conversion endpoint accepts the required currency and amount information and returns the converted result.

The endpoint uses the exchange-rate API and includes a Frankfurter fallback.

---

## Search History

GET:

`/api/history`

Returns stored search history from SQLite.

---

## Random Country

GET:

`/api/random`

Returns a random country from the database.

---

# 🖥️ Main Website Routes

The Flask application contains the following main pages:

`/`

Home page

`/countries`

Countries page

`/compare`

Country comparison

`/convert`

Currency conversion

`/random`

Random country

`/health`

Application health check

---

# ❤️ Health Check

Live health endpoint:

https://yatharthkale.pythonanywhere.com/health

This endpoint can be used to check whether the deployed Flask application is running.

---

# 🔄 Data Flow

## Country Information

User → Frontend → Flask Backend → SQLite Database → Flask Backend → Frontend

## Weather

User → Frontend → Flask Backend → Open-Meteo API → Flask Backend → Frontend

## Currency

User → Frontend → Flask Backend → Exchange Rate API → Flask Backend → Frontend

If the primary currency API is unavailable, the backend can use Frankfurter as a fallback.

---

# 📦 Python Requirements

The project uses:

```text
Flask==3.0.3
requests
