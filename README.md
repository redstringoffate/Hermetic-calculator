# Hermetic-calculator
Hermetic Lot calculator without ephemeris or birth data dependencies.

# Hermetic Lot Calculator

A lightweight Streamlit web app for calculating core **Hermetic Lots**  
using manually entered zodiac positions (down to seconds).

This tool intentionally avoids ephemeris calculations and focuses on
**transparent, traditional formulas**.

---

## Features

- Calculates the core Hermetic Lots:
  - Fortune
  - Spirit
  - Eros
  - Courage (Andreia)
  - Victory (Nike)
  - Necessity (Ananke)
  - Nemesis
- Supports **Day / Night (Sect)** logic
- Input via **Sign / Degree / Minute / Second**
- Outputs results in a clean, readable format (e.g. Fortune: Leo, 4°54'07'')

- No Swiss Ephemeris, no birth data required

---

## Tech Stack

- Python
- Streamlit

---

## Project Structure

├─ app.py # Streamlit UI
├─ hermetic_lots.py # Hermetic Lot calculations
├─ utils.py # Angle conversions & formatting
├─ constants.py # Zodiac signs & lot definitions



---

## How to Run

```bash
pip install -r requirements.txt
streamlit run app.py


