# 🔥 Wildfire Guardian — Real-Time Crisis Response Assistant

A real-time, AI-powered wildfire alert and response platform that aggregates public data sources, delivers actionable SMS alerts, and provides an interactive crisis map — starting with U.S. wildfires.

---

## Problem

Wildfires in the U.S. are increasing in frequency and intensity (~70,000/year, 7M+ acres burned). Existing alert systems are slow, fragmented, and lack actionable guidance. People affected by wildfires need fast, clear answers: *Where is the fire? What should I do? Where do I go?*

## Solution

Wildfire Guardian combines official data feeds, AI-driven guidance, and crowdsourced updates into a single platform that:

- **Aggregates real-time wildfire data** from NOAA, USGS, and NASA FIRMS on a 15-minute refresh cycle
- **Sends SMS alerts** with clear evacuation instructions and shelter locations via Twilio
- **Displays a live interactive map** of active fires, shelters, and road closures
- **Answers natural-language questions** through an AI chatbot (e.g., "Is my zip code safe?")
- **Accepts crowdsourced reports** from users (road closures, safe zones) with verification

---

## Architecture

```
NOAA / USGS / NASA FIRMS
        │
        ▼
  FastAPI (Ingestion)  ──►  Supabase (Postgres)
        │                        │
        ▼                        ▼
  Twilio (SMS Alerts)     Streamlit + Leaflet.js (Map UI)
                                 │
                                 ▼
                        Hugging Face (AI Chatbot)
```

**Data Flow:**
1. FastAPI pulls wildfire data from public APIs every 15 minutes → stores in Supabase
2. Geospatial queries detect fires near registered users → triggers Twilio SMS alerts
3. Streamlit web app renders a live Leaflet.js map with fire perimeters, shelters, and closures
4. AI chatbot (Hugging Face NLP) responds to user questions via SMS or web

---

## Tech Stack

| Layer       | Tool                  | Purpose                            |
|-------------|-----------------------|------------------------------------|
| Backend     | FastAPI (Python)      | Data ingestion, alert logic, API   |
| Database    | Supabase (Postgres)   | Users, fires, alerts, user reports |
| Messaging   | Twilio                | SMS alerts and chatbot interaction |
| Frontend    | Streamlit + Leaflet.js| Live crisis map and web interface  |
| AI/NLP      | Hugging Face          | Chatbot for natural-language Q&A   |
| Data Sources| NOAA, USGS, NASA FIRMS| Fire weather, perimeters, hotspots |

---

## Data Sources

| Source       | Data Provided          | Link                                                              |
|--------------|------------------------|-------------------------------------------------------------------|
| NOAA/NWS     | Fire weather alerts    | [api.weather.gov](https://www.weather.gov/documentation/services-web-api) |
| USGS GeoMAC  | Fire perimeters        | [USGS GeoMAC](https://rmgsc.cr.usgs.gov/outgoing/GeoMAC/)       |
| NASA FIRMS   | Real-time fire hotspots| [NASA FIRMS](https://firms.modaps.eosdis.nasa.gov/)              |
| OpenStreetMap| Base maps + shelters   | [openstreetmap.org](https://www.openstreetmap.org/)              |

---

## Database Schema

Core tables in Supabase Postgres:

- **`users`** — phone number, zip code, lat/lng, SMS opt-in status
- **`fires`** — name, coordinates, size (acres), containment %, source, last updated
- **`alerts`** — links user ↔ fire, message text, delivery status
- **`user_reports`** — crowdsourced updates (road closures, safe zones) with verification flag

---

## Roadmap

- [x] Project scoping and architecture design
- [ ] Supabase database setup
- [ ] Data ingestion pipeline (NOAA / USGS / NASA → Supabase)
- [ ] SMS alert system (Twilio + geospatial proximity logic)
- [ ] Live map prototype (Streamlit + Leaflet.js)
- [ ] AI chatbot integration (Hugging Face)
- [ ] User testing pilot (1,000+ users in CA/OR)
- [ ] Crowdsourced reporting and verification
- [ ] Expand to floods, hurricanes, earthquakes, geopolitical events
---

## License

MIT

---

## Author

**Daniel Brown**
