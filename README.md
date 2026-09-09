# 🌍 WorldInfo

WorldInfo is a Python Flask web application that provides country information, country comparison, currency conversion, and weather information.

## 🚀 Live Website

https://yatharthkale.pythonanywhere.com/

## 🛠️ Technologies Used

- Python
- Flask
- SQLite
- HTML
- CSS
- REST APIs
- JSON

## ⚙️ Backend Architecture

Browser
↓
Flask (Python)
↓
├── SQLite Database
├── Currency API
└── Open-Meteo Weather API

## 🌦️ Weather

Weather information is retrieved through the Open-Meteo API.

## 💱 Currency Converter

Currency conversion uses an external exchange-rate API with a fallback service.

## 🗄️ Database

SQLite is used to store structured country information and application data.

## 🔌 API Endpoints

### Country

/api/country/India

### Countries

/api/countries

### Weather

/api/weather/India

### Currency

/api/convert?from=USD&to=INR&amount=100

### Health

/health

## 📁 Project Structure

worldinfo_api.py
worldinfo.db

## 👨‍💻 Project

WorldInfo is developed using Python Flask and deployed on PythonAnywhere.
