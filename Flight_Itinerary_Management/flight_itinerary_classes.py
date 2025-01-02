'''
Flight and Itinerary Classes

This program models a flight and a travel itinerary, providing functionality to calculate total flight time and total travel time for multiple flights.

## Classes

### 1. `Flight`
Represents an individual flight with attributes:
- `flight_number`: The flight's identification number (string).
- `departure_time`: The departure time of the flight (`datetime` object).
- `arrival_time`: The arrival time of the flight (`datetime` object).

Methods:
- `get_departure_time()`: Returns the departure time of the flight.
- `get_arrival_time()`: Returns the arrival time of the flight.
- `get_flight_time()`: Calculates and returns the flight duration in minutes.

### 2. `Itinerary`
Represents an itinerary composed of multiple flights with attributes:
- `flights`: A list of `Flight` objects.

Methods:
- `getTotalFlightTime()`: Calculates and returns the total flight time for all flights in the itinerary.
- `getTotalTravelTime()`: Calculates and returns the total travel time (including layovers) from the departure of the first flight to the arrival of the last flight.

## Main Function
1. Creates a list of `Flight` objects with specified flight numbers, departure times, and arrival times.
2. Constructs an `Itinerary` object using the list of flights.
3. Prints:
   - Total travel time (including layovers) in minutes.
   - Total flight time (excluding layovers) in minutes.

## Example Usage
Total Travel Time: 470.0 minutes Total Flight Time: 235.0 minutes


## Applications
- Modeling and analysis of travel itineraries.
- Calculating total travel and flight durations for logistics and scheduling.
- Demonstrates use of object-oriented programming and `datetime` operations in Python.
'''

from datetime import datetime

class Flight ():
    def __init__(self, flight_number, departure_time, arrival_time):
        self.flight_number = str(flight_number)
        self.departure_time = departure_time
        self.arrival_time = arrival_time



    def flight_number(self):
        return self.flight_number

    def get_departure_time(self):
        return self.departure_time

    def get_arrival_time(self):
        return self.arrival_time

    def get_flight_time(self):
        flight_time = self.arrival_time - self.departure_time
        return flight_time.total_seconds()/60


class Itinerary():
    def __init__(self, flights):
        self.flights = flights

    def getTotalFlightTime (self):
        total_flight_time = sum(flight.get_flight_time() for flight in self.flights)
        return total_flight_time

    def getTotalTravelTime(self):
        departure_time = self.flights[0].get_departure_time()
        arrival_time = self.flights[-1].get_arrival_time()
        total_travel_time = (arrival_time - departure_time).total_seconds()/60
        return total_travel_time


def main():

    flights = []

    flights.append(Flight("US230",

        datetime(2014, 4, 5, 5, 5, 0),

        datetime(2014, 4, 5, 6, 15, 0)))

    flights.append(Flight("US235",

        datetime(2014, 4, 5, 6, 55, 0),

        datetime(2014, 4, 5, 7, 45, 0)))

    flights.append(Flight("US237",

        datetime(2014, 4, 5, 9, 35, 0),

        datetime(2014, 4, 5, 12, 55, 0)))

   

    itinerary = Itinerary(flights)

    print(itinerary.getTotalTravelTime())

    print(itinerary.getTotalFlightTime())

main()





    