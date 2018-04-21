package common;

public class validations {

    protected boolean isValidDate(int day, int month, int year) {

        final int MIN_YEAR = 2018;
        final int MAX_YEAR = 2100;
        final int MAX_MONTH = 12;
        final int FEB = 2;
        final int APR = 4;
        final int JUN = 6;
        final int SEP = 9;
        final int NOV = 11;

        int maxDay = 31;

        // Valid year
        if ((year >= MIN_YEAR) && (year <= MAX_YEAR)) {
            // Valid month
            if ((month <= MAX_MONTH) && (month > 0)) {

                // Max day corner cases
                if ((month == APR) || (month == JUN) || (month == SEP) || (month == NOV)) {
                    maxDay = 30;
                } else if ((month == FEB)) {
                    if ((year % 4 == 0)) {
                        maxDay = 29;
                    } else {
                        maxDay = 28;
                    }
                }
                // Valid day
                if ((day <= maxDay) && (day > 0)) {
                    // return True
                    return true;
                }
            }
        }
        // return False
        return false;
    }

    protected String isValidName(String name) {
        final String DEFAULT_NAME = "NoName";

        if (name.isEmpty()) {
            return DEFAULT_NAME;
        }
        return name;
    }

    protected int isValidNumOfCountries(int numOfCountries) {
        final int MAX_COUNTRIES = 10;

        if (numOfCountries > MAX_COUNTRIES || (numOfCountries <= 0)) {
            return MAX_COUNTRIES;
        }
        return numOfCountries;
    }

    protected int isValidNumOfTravellers(int numOfTravellers) {
        final int MAX_TRAVELLERS = 50;

        if ((numOfTravellers > MAX_TRAVELLERS) || (numOfTravellers <= 0)) {
            return MAX_TRAVELLERS;
        }
        return numOfTravellers;
    }
}
