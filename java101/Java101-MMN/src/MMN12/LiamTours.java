package MMN12;

public class LiamTours {

    private final int MAX_TRIPS = 100;

    private Trip[] _data;
    private int _noOfTrips;

    public LiamTours() {
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

    public int howManyTravellers(){
        int travellerSum  = 0;

        for (Trip a_trip : _data) {
            travellerSum += a_trip.getNoOfTravellers();
        }
        return travellerSum;
    }

    public int howManyTripDeparture(Date reqDate){
        int tripSum = 0;

        for (Trip a_trip : _data) {
            if (a_trip.getDepartureDate().equals(reqDate)) {
                tripSum++;
            }
        }
        return tripSum;
    }

    public int howManyCars(Date reqDate){
        int carSum = 0;

        for (Trip a_trip : _data) {
            if (a_trip.getDepartureDate().equals(reqDate)) {

                carSum += a_trip.howManyCars();
            }
        }
        return carSum;
    }

    public Trip longestTrip(){

        if (_data.length != 0) {
            int theLongestTripId = 0;
            int theLongestTripDuration = 0;

            for (int i = 0; i < _data.length; i++) {
                if (_data[i].tripDuration() > theLongestTripDuration) {
                    theLongestTripId = i;
                }
            }
            return _data[theLongestTripId];
        }
    }

    public Trip mostPopularGuide(){

        if (_data.length != 0) {
            int theGuideId = 0;
            int noOfGuides = ;
            int theGuideTripSum = 0;

            for (int i = 0; i < _data.length; i++) {
                if (_data[i].getGuideName() > theGuideTripSum) {
                    theGuideId = i;
                }
            }
            return _data[theGuideId];
        }
    }
}
