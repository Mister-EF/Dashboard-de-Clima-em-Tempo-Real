# Real-Time Weather Dashboard

An integrated project using a Python backend to securely fetch data from external APIs and a JavaScript frontend to render dynamic weather icons and live temperature data. Type a city, get the current conditions — instantly.

---

## How It Works

The frontend sends the city name to the Flask backend via a `POST` request. Python first hits the Open-Meteo Geocoding API to resolve the city into coordinates, then queries the Open-Meteo Forecast API for current weather data. The response is sent back to the browser, where JavaScript renders the temperature, wind speed, and a condition icon dynamically — no page reload required.

---

## Built With

| Technology | Role |
|------------|------|
| Python | Backend API orchestration and data routing |
| Flask | REST endpoint serving weather data to the frontend |
| `requests` | HTTP calls to the Open-Meteo geocoding and forecast APIs |
| JavaScript | Async fetch, DOM updates, and weather icon rendering |
| HTML/CSS | Glassmorphism card layout and input styling |

---

## External APIs Used

| API | Purpose |
|-----|---------|
| Open-Meteo Geocoding | Resolves city name to latitude and longitude |
| Open-Meteo Forecast | Returns current temperature, wind speed, and weather code |

Both APIs are free and require no authentication key.

---

## Project Structure

```
/
├── app.py                # Flask server with /clima POST endpoint
└── template/
    └── index.html        # Weather card UI with inline JS and CSS
```

---

## Getting Started

**1. Install dependencies**

```bash
pip install flask requests
```

**2. Start the server**

```bash
python app.py
```

**3. Open the dashboard**

Navigate to `http://127.0.0.1:5000` and search for any city.

---

## API Reference

**`POST /clima`**

Request body:
```json
{ "cidade": "Cidade" }
```

Success response:
```json
{
  "cidade": "Cidade",
  "estado": "Estado",
  "temp": 24.5,
  "wind": 12.3,
  "code": 1
}
```

---

## Weather Conditions

| Code Range | Status | Icon |
|------------|--------|------|
| `0` | Clear Sky | ☀️ |
| `1 – 3` | Partly Cloudy | ⛅ |
| `45+` | Fog or Rain | 🌧️ |

---

## Features

- Two-step API chain: geocoding first, then forecast — all handled server-side
- Dynamic weather icon and condition label rendered from WMO weather codes
- Glassmorphism card UI with `backdrop-filter` and semi-transparent borders
- Graceful error handling for unknown cities and connection failures
- No API key required — fully open and free to run

Thank you for your attention!
