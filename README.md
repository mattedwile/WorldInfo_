# 🌍 WorldInfo

WorldInfo is a Python Flask web application that provides country information, country comparison, currency conversion, weather information, and other country-based features.

The project uses **Python + Flask + SQLite + HTML/CSS**, with external APIs integrated for live currency exchange rates and weather data.

---

## 🔗 Project Links

### GitHub Repository
https://github.com/yatharthkale/WorldInfo

### Live Website
https://yatharthkale.pythonanywhere.com/

### Main Backend File
https://github.com/yatharthkale/WorldInfo/blob/main/worldinfo_api.py

---

# 🎯 Project Objective

The main objective of WorldInfo is to provide useful country-related information through a simple web interface.

The application combines:

- Country information
- Country comparison
- Currency conversion
- Weather information
- Search history
- Random country selection
- REST API endpoints
- SQLite database
- External live APIs

---

# 🛠️ Technologies Used

| Technology | Purpose |
|---|---|
| Python | Main programming language |
| Flask | Backend web framework |
| SQLite | Database |
| HTML | Frontend structure |
| CSS | Frontend styling |
| Requests | Connecting Flask with external APIs |
| Open-Meteo API | Live weather data |
| Exchange Rate API | Live currency exchange rates |
| PythonAnywhere | Deployment |
| GitHub | Source code management |

---

# 🏗️ Basic Architecture

```text
User
  ↓
HTML / CSS Frontend
  ↓
Flask Backend
  ↓
 ┌───────────────────────┐
 │                       │
SQLite Database       External APIs
 │                       │
 │                 ┌─────┴──────────┐
 │                 │                │
 │            Weather API     Currency API
 │            Open-Meteo      ExchangeRate
 │
 ↓
Backend processes data
  ↓
Frontend displays result
