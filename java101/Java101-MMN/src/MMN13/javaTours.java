package MMN13;

import MMN12.Date;
import MMN12.Trip;

import java.util.HashMap;
import java.util.Map;

public class javaTours {

    private final int MAX_TRIPS = 100;

    private Trip[] _data;
    private int _noOfTrips;

    public javaTours() {
        _data = new Trip[MAX_TRIPS];
        _noOfTrips = 0;
    }

    public int getNoOfTrips() {
        return _noOfTrips;
    }

    public boolean addTrip(Trip newTrip) {

        if (_data.length != 0) {
            _data[_noOfTrips++] = newTrip;
            return true;
        }
        return false;
    }

    public boolean removeTrip(Trip tripToRemove) {

        if (_data.length != 0) {
            for (int i = 0; i < _data.length; i++) {
                if (_data[i].equals(tripToRemove)) {
                    for (int j = i; j < _noOfTrips - 1; j++) {
                        _data[j] = _data[j + 1];
                    }
                    _data[_noOfTrips - 1] = null;
                    _noOfTrips--;
                }
            }
        }
        return false;
    }

    public int howManyTravellers() {
        int travellerSum = 0;

        for (Trip a_trip : _data) {
            travellerSum += a_trip.getNoOfTravellers();
        }
        return travellerSum;
    }

    public int howManyTripDeparture(Date reqDate) {
        int tripSum = 0;

        for (Trip a_trip : _data) {
            if (a_trip.getDepartureDate().equals(reqDate)) {
                tripSum++;
            }
        }
        return tripSum;
    }

    public int howManyCars(Date reqDate) {
        int carSum = 0;

        for (Trip a_trip : _data) {
            if (a_trip.getDepartureDate().equals(reqDate)) {

                carSum += a_trip.howManyCars();
            }
        }
        return carSum;
    }

    public Trip longestTrip() {
        int theLongestTripId = 0;
        int theLongestTripDuration = 0;

        if (_data.length != 0) {
            for (int i = 0; i < _data.length; i++) {
                if (_data[i].tripDuration() > theLongestTripDuration) {
                    theLongestTripId = i;
                }
            }
        }
        return _data[theLongestTripId];
    }

    public String mostPopularGuide() {
        String popGuide = "0";

        if (_data.length != 0) {

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
        }
        // Return the guide with the most trips
        return popGuide;
    }
}
