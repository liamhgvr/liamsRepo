package MMN12;

import common.validations;

public class Trip extends validations {

    // declarations
    final int MAX_COUNTRIES = 10;
    final int MAX_TRAVELLERS = 50;
    final int PRICE_PER_DAY = 250;
    final int PRICE_PER_COUNTRY = 100;
    final int BUS_SIZE = 10;
    final int HIGH_SEASON = 20;

    private String _guideName;
    private Date _departureDate;
    private Date _returningDate;
    private int _noOfCountries;
    private int _noOfTravellers;

    // constructors
    public Trip(String guideName, int depDay, int depMonth, int depYear, int retDay, int retMonth, int retYear,
                int countryNum, int travellersNum) {

        _guideName = isValidName(guideName);

        _noOfCountries = isValidNumOfCountries(countryNum);
        _noOfTravellers = isValidNumOfTravellers(travellersNum);

        _departureDate = new Date(depDay, depMonth, depYear);
        _returningDate = new Date(retDay, retMonth, retYear);

        // set dates to default if error
        if (_departureDate.after(_returningDate)) {
            _departureDate = new Date();
            _returningDate = new Date();
        }
    }

    public Trip(Trip other) {

        _guideName = isValidName(other.getGuideName());

        _noOfCountries = isValidNumOfCountries(other.getNoOfCountries());
        _noOfTravellers = isValidNumOfTravellers(other.getNoOfTravellers());

        _departureDate = other.getDepartureDate();
        _returningDate = other.getReturningDate();

        // set dates to default if error
        if (_departureDate.after(_returningDate)) {
            _departureDate = new Date();
            _returningDate = new Date();
        }
    }

    // Get methods
    public String getGuideName() {
        return _guideName;
    }

    public Date getDepartureDate() {
        return _departureDate;
    }

    public Date getReturningDate() {
        return _returningDate;
    }

    public int getNoOfCountries() {
        return _noOfCountries;
    }

    public int getNoOfTravellers() {
        return _noOfTravellers;
    }

    // Set methods

    public void set_guideName(String newName){
        if (!newName.isEmpty()){
            _guideName = newName;
        }
    }

    public void set_departureDate(Date other) {
        if (isValidDate(other.getDay(), other.getMonth(), other.getYear()) && _returningDate.after(other)) {
            _departureDate = new Date(other);
        }
    }

    public void set_returningDate(Date other) {
        if (isValidDate(other.getDay(), other.getMonth(), other.getYear()) && _departureDate.before(other)) {
            _returningDate = new Date(other);
        }
    }

    public void set_noOfCountries(Date other) {
        if (isValidDate(other.getDay(), other.getMonth(), other.getYear()) && _departureDate.before(other)) {
            _returningDate = new Date(other);
        }
    }

    public void set_noOfCountries(int newNoOfCountries) {
        if (newNoOfCountries < MAX_COUNTRIES && newNoOfCountries > 0) {
            _noOfCountries = newNoOfCountries;
        }
    }

    public void set_noOfTravellers(int newNoOfTravellers) {
        if (newNoOfTravellers < MAX_TRAVELLERS && newNoOfTravellers > 0) {
            _noOfCountries = newNoOfTravellers;
        }
    }

    // Operation methods

    public boolean equals(Trip other) {
        return _guideName.equals(other.getGuideName()) && _departureDate.equals(other.getDepartureDate()) &&
                _returningDate.equals(other.getReturningDate()) && _noOfCountries == other.getNoOfCountries() &&
                _noOfTravellers == other.getNoOfTravellers();
    }

    public boolean sameDepartureDate(Date other) {
        return _departureDate.equals(other);
    }

    public boolean sameReturningDate(Date other) {
        return _returningDate.equals(other);
    }

    public boolean overlap(Trip other) {
        return _departureDate.after(other.getReturningDate()) ||
                _returningDate.before(other.getDepartureDate()); // check if trips overlap
    }

    public int tripDuration() {
        if (_departureDate.equals(_returningDate)) { // Single day scenario
            return 1;
        }
        return _departureDate.difference(_returningDate); // return trip duration
    }

    public boolean isLoaded() {
        return _noOfCountries > this.tripDuration(); // check if countries are more than trip duration
    }

    public int howManyCars() {
        int noOfBuses = _noOfTravellers / BUS_SIZE;

        if (_noOfTravellers % BUS_SIZE > 0) {
            noOfBuses += 1;
        }

        return noOfBuses;
    }

    public double calculatePrice() {
        double price = this.tripDuration() * PRICE_PER_DAY + this._noOfCountries * PRICE_PER_COUNTRY;

        if (_departureDate.getMonth() == 7 || _departureDate.getMonth() == 8) {
            price = price * 1.2;
        }

        return price;
    }

    public String toString() {
        return "TRIP: " + _guideName + "|" + _departureDate.toString() + "|" + _returningDate.toString() +
                "|" + _noOfCountries + "|" + _noOfTravellers;
    }
}
