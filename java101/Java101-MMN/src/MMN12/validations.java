package MMN12;

public class validations {

    public boolean isValidDate(int day, int month, int year) {

        final int MAX_MONTH = 12;
        final int FEB = 2;
        final int APR = 4;
        final int JUN = 6;
        final int SEP = 9;
        final int NOV = 11;

        int maxDay = 31;

        // Validate positive
        if ((year > 0) && (month > 0) && (day > 0)) {
            // Validate month
            if (month <= MAX_MONTH) {
                // Day corner cases
                if ((month == APR) || (month == JUN) || (month == SEP) || (month == NOV)) {
                    maxDay = 30;
                } else if ((month == FEB)) {
                    if ((year % 4 == 0) || (year == 400)) {
                        maxDay = 29;
                    } else {
                        maxDay = 28;
                    }
                }
                // Validate day
                if (day <= maxDay) {
                    // return True
                    return true;
                }
            }
        }
        // return False
        return false;
    }

    public String isValidName(String name){
        final String DEFAULT_NAME = "NoName";

        if (name.isEmpty()){
            return DEFAULT_NAME;
        }
        return name;
    }

    public int isValidNumOfCountrues(int numOfCountries){
        final int MAX_COUNTRIES = 10;

        if (numOfCountries > MAX_COUNTRIES){
            return MAX_COUNTRIES;
        }
        return numOfCountries;
    }

    public int isValidNumOfTravellers(int numOfTravellers){
        final int MAX_TRAVELLERS = 50;

        if (numOfTravellers > MAX_TRAVELLERS){
            return MAX_TRAVELLERS;
        }
        return numOfTravellers;
    }
}
