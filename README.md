# RIT Optimal Gym Time Finder

RIT Optimal Gym Time Finder is a Python-based data pipeline that collects publicly available gym occupancy data from RIT’s facility occupancy tracker and analyzes it to determine the least crowded times to work out.

The project is designed to answer a simple question: **when is the gym typically the least busy?**

---

## Motivation

Nobody likes walking into a packed gym and waiting 20 minutes for a squat rack.  
This project automates the process of collecting and analyzing occupancy data so gym visits can be planned during off-peak hours.

---

## How It Works

### 1. Data Collection
- `scrape.py` periodically scrapes the publicly available RIT gym occupancy tracker
- Each scrape records a timestamp and current occupancy
- Data is appended to a CSV file, forming a time-series dataset

### 2. Data Analysis
- `analysis.py` reads the collected CSV data
- Occupancy values are grouped by time of day across multiple days
- Average occupancy is computed for each time slot

### 3. Visualization
- A plot is generated showing average gym occupancy by time of day
- This makes peak and off-peak hours easy to identify at a glance

---

## Assumptions and Notes

- Gym operating hours are assumed to be **6:00 AM – 11:00 PM** on weekdays and **10:00 AM - 11:00 PM** on weekends
- Data is collected at approximately **30-minute intervals**  
  (minor timing drift may occur due to request and processing time)
- Analysis logic was validated using **synthetic data** prior to collecting real data
- The scraper is designed to work with real data collected over multiple days
- Analysis assumes complete daliy coverage; partial days may skew averages

---

## How to Run

1. Run the scraper to collect data:
   - Start `scrape.py` and allow it to run for a period of time
   - Data will be written to a CSV file

2. Run the analysis:
   - Execute `analysis.py` to generate a visualization of average occupancy by time of day

---

## Future Improvements

- Deploy the scraper on an always-on host for continuous data collection
- Collect data over longer time spans for stronger statistical trends
- Add additional analysis such as weekday vs weekend comparisons
