package MMN13;

import MMN12.Date;
import MMN12.Trip;

import java.util.HashMap;
import java.util.Map;

public class javaTours {

    private final int MAX_TRIPS = 100;
    private Trip[] _data;
    private int _noOfTrips;

    // Constructor
    public javaTours() {
        _data = new Trip[MAX_TRIPS];
        _noOfTrips = 0;
    }

    // Get methods
    public int getNoOfTrips() { // Returns the total number of trips
        return _noOfTrips;
    }

    // Modify methods
    public boolean addTrip(Trip newTrip) { // Adds a given trip

        if (_noOfTrips < MAX_TRIPS) {
            _data[_noOfTrips] =  new Trip(newTrip);
            _noOfTrips++;
            return true;
        }
        return false;
    }

    public boolean removeTrip(Trip tripToRemove) { // Removes a given trip

        if (_noOfTrips > 0) {
            for (int i = 0; i < _data.length; i++) {
                if (_data[i].equals(tripToRemove)) {
                    System.arraycopy(_data, i + 1, _data, i, _noOfTrips - 1 - i);
                    _data[_noOfTrips - 1] = null;
                    _noOfTrips--;
                }
            }
        }
        return false;
    }

    // Stat methods
    public int howManyTravellers() { // Return the total number of travellers in all trips
        int travellersCount = 0;

        if (_noOfTrips > 0){
            for (Trip trip : _data) travellersCount += trip.getNoOfTravellers();
        }
        return travellersCount;
    }

    public int howManyTripDepartures(Date reqDate) { // Returns the number of trips that depart on a given date
        int tripCount = 0;

        if (_noOfTrips > 0){
            for (Trip trip : _data) {
                if (trip.getDepartureDate().equals(reqDate)) {
                    tripCount++;
                }
            }
        }
        return tripCount;
    }

    public int howManyCars(Date reqDate) { // Returns the number of cars needed for all trips on a given date
        int carSum = 0;

        if (_noOfTrips > 0){
            for (Trip trip : _data) {
                if (trip.getDepartureDate().equals(reqDate)) {

                    carSum += trip.howManyCars();
                }
            }
        }
        return carSum;
    }

    public Trip longestTrip() { // Returns the longest trip in _data

        if (_noOfTrips == 0) {
            System.out.println("No trips available.");
            return null;
        }else {
            int theLongestTripId = 0;
            int theLongestTripDuration = 0;

            for (int i = 0; i < _data.length; i++) {
                if (_data[i].tripDuration() > theLongestTripDuration) {
                    theLongestTripId = i;
                }
            }
            // Return the longest trip
            return _data[theLongestTripId];
        }
    }

    public String mostPopularGuide() { // Returns the guides who is has the most trips

        if (_noOfTrips == 0) {
            System.out.println("No trips available.");
            return null;
        } else {
            String popGuide = "no name";

            // Count tripe
            String currGuide = _data[0].getGuideName();
            HashMap<String, Integer> countGuideTrips = new HashMap<String, Integer>();
            countGuideTrips.put(currGuide, 1);

            for (Trip trip : _data) {
                currGuide = trip.getGuideName();

                if (countGuideTrips.containsKey(trip.getGuideName())) {
                    countGuideTrips.put(currGuide, countGuideTrips.get(currGuide) + 1);
                } else {
                    countGuideTrips.put(currGuide, 1);
                }
            }

            // Compare trips
            int maxTrips = 0;

            for (Map.Entry<String, Integer> entry : countGuideTrips.entrySet()) {
                if (maxTrips == 0 || entry.getValue() > maxTrips) {
                    maxTrips = entry.getValue();
                }
            }
            // Return the guide with the most trips
            return popGuide;
        }
    }

    public Trip earliestTrip() { // Returns the earliest trip
        if (_noOfTrips == 0) {
            System.out.println("No trips available.");
            return null;
        } else {
            int earliestTripID = 0;
            Date tripDate = null;

            for (int i = 0; i < _data.length; i++) {

                if (i == 0) {
                    tripDate = _data[i].getDepartureDate();
                } else {
                    if (_data[i].getDepartureDate().before(tripDate)) {
                        earliestTripID = i;
                    }
                }
            }
            // Return the most expensive trip
            return _data[earliestTripID];
        }
    }

    public Trip mostExpensiveTrip() {

        if (_noOfTrips == 0) {
            System.out.println("No trips available.");
            return null;
        } else {
            int mostExpensiveTripID = 0;
            double tripCost = 0;

            for (int i = 0; i < _data.length; i++) {
                if (i == 0) {
                    tripCost = _data[i].calculatePrice();
                } else {
                    if (_data[i].calculatePrice() > tripCost) {
                        mostExpensiveTripID = i;
                    }
                }
            }
            // Return the most expensive trip
            return _data[mostExpensiveTripID];
        }
    }
}
