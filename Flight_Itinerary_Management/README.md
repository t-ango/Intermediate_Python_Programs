# Flight and Itinerary Management

This folder contains a Python implementation of `Flight` and `Itinerary` classes to model individual flights and multi-flight travel itineraries. 
The program calculates total flight time and total travel time for an itinerary.

---

## Features

1. **Flight Class**:
   - Represents a single flight with:
     - Flight number.
     - Departure time.
     - Arrival time.
   - Calculates the flight duration in minutes.

2. **Itinerary Class**:
   - Represents a series of connected flights.
   - Calculates:
     - Total flight time (sum of flight durations).
     - Total travel time (including layovers).

3. **Time Calculations**:
   - Uses Python's `datetime` module for accurate time-based operations.

---

## How to Run
1. Run the program:
   ```bash
   python3 flight_itinerary.py
   
2. View the output, including:
Total travel time (in minutes).
Total flight time (in minutes).

**Example Usage**

Input: The program defines three sample flights:

Flight US230: Departure at 5:05 AM, Arrival at 6:15 AM.
Flight US235: Departure at 6:55 AM, Arrival at 7:45 AM.
Flight US237: Departure at 9:35 AM, Arrival at 12:55 PM.
Output:

Total Travel Time: 470.0 minutes
Total Flight Time: 235.0 minutes

**Applications**

Travel Planning:
Calculate travel times for itineraries with multiple connecting flights.
Logistics and Scheduling:
Useful for airlines or travel agencies to optimize schedules.
Educational Tool:
Demonstrates object-oriented programming and time calculations in Python.

**Requirements**

Python 3.x
datetime module (part of Python standard library)
