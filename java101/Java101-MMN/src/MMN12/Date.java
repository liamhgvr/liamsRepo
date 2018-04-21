package MMN12;

import common.validations;

public class Date extends validations {

    // declarations
    private final int DEFAULT_DAY = 1;
    private final int DEFAULT_MONTH = 1;
    private final int DEFAULT_YEAR = 1990;
    private int _day;
    private int _month;
    private int _year;

    // constructors
    public Date(){
        _day = DEFAULT_DAY;
        _month = DEFAULT_MONTH;
        _year = DEFAULT_YEAR;
    }

    public Date(int day, int month, int year){
        if (isValidDate(day, month, year)){
            _day = day;
            _month = month;
            _year = year;
        } else {
            _day = DEFAULT_DAY;
            _month = DEFAULT_MONTH;
            _year = DEFAULT_YEAR;
        }
    }

    public Date(Date other) {
        if (isValidDate(other._day, other._month, other._year)){
            _day = other._day;
            _month = other._month;
            _year = other._year;
        } else {
            _day = DEFAULT_DAY;
            _month = DEFAULT_MONTH;
            _year = DEFAULT_YEAR;
        }
    }

    // methods
    public int getDay(){ return _day; }

    public int getMonth(){ return _month; }

    public int getYear(){ return _year; }

    public void set_day(int newDay){
        if (isValidDate(newDay, _month, _year)){
            _day = newDay;
        }
    }

    public void set_month(int newMonth){
        if (isValidDate(_day, newMonth, _year)){
            _month = newMonth;
        }
    }

    public void set_year(int newYear){
        if (isValidDate(_day, _month, newYear)){
            _year = newYear;
        }
    }

    public boolean equals(Date other){
        // Verify dates are the same
        return calculateDate(other.getDay(), other.getMonth(), other.getYear()) == calculateDate(_day, _month, _year);
    }

    public boolean before(Date other){
        // Verify object date is  prior to given date
        return calculateDate(other.getDay(), other.getMonth(), other.getYear()) > calculateDate(_day, _month, _year);
    }

    public boolean after(Date other){
        // verify object date is later than given date
        return !before(other);
    }

    public int difference(Date other){
        // return difference in days
        int dif = calculateDate(other.getDay(), other.getMonth(), other.getYear()) - calculateDate(_day, _month, _year);

        if (dif < 0){
            dif *= -1;
        }
        return dif;
    }

    public String toString(){
        return "" + _day + "/" + _month + "/" + _year + "";
    }

    static int calculateDate(int day, int month, int year){
        if (month < 3){
            year--;
            month = month + 12;
        }
        // return number of days from form BOC
        return 365 * year + year/4 - year/100 + year/400 + ((month+1) * 306)/10 + (day - 62);
    }
}
