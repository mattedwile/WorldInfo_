# 🌍 WorldInfo

### Country Information • Comparison • Weather • Currency

WorldInfo is a Python Flask web application designed to explore and compare countries while providing weather information and currency conversion.

---

## 🚀 Live Demo

👉 https://yatharthkale.pythonanywhere.com/

---

## ✨ Features

- 🌍 Country information
- ⚖️ Country comparison
- 🌦️ Weather information
- 💱 Currency conversion
- 🔎 Country search
- 🎲 Random country
- 📊 JSON API endpoints
- 🗄️ SQLite database
- ☁️ Cloud deployment

---

## 🛠️ Technologies

| Technology | Purpose |
|---|---|
| Python | Backend programming |
| Flask | Web framework & API |
| SQLite | Database |
| HTML | Website structure |
| CSS | Website design |
| REST APIs | External/live data |
| JSON | Data exchange |

---

## 🏗️ Architecture

```text
                    USER
                     │
                     ▼
                 WEB BROWSER
                     │
                     ▼
              ┌──────────────┐
              │ Flask / Python│
              │   Backend    │
              └──────┬───────┘
                     │
          ┌──────────┼──────────┐
          ▼          ▼          ▼
       SQLite     Currency    Weather
      Database       API         API
          │          │            │
          ▼          ▼            ▼
      Country     Exchange     Open-Meteo
       Data        Rates
