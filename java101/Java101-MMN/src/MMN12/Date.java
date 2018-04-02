package MMN12;

public class Date extends validations {

    // declarations
    private int _day;
    private int _month;
    private int _year;

    // constructors
    public Date(){
        _day = 1;
        _month = 1;
        _year = 2000;
    }

    public Date(int day, int month, int year){
        if (isValidDate(day, month, year)){
            _day = day;
            _month = month;
            _year = year;
        }
    }

    public Date(Date other) {
        if (isValidDate(other._day, other._month, other._year)){
            _day = other._day;
            _month = other._month;
            _year = other._year;
        }
    }

    // methods
    public int getDay(){ return _day; }

    public int getMonth(){ return _month; }

    public int getYear(){ return _year; }

    public void setDay(int newDay){
        if (isValidDate(newDay, _month, _year)){
            _day = newDay;
        }
    }

    public void setMonth(int newMonth){
        if (isValidDate(_day, newMonth, _year)){
            _month = newMonth;
        }
    }

    public void setYear(int newYear){
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

    // given
    private static int calculateDate(int day, int month, int year){
        if (month < 3){
            year--;
            month = month + 12;
        }
        // return number of days from form BOC
        return 365 * year + year/4 - year/100 + year/400 + ((month+1) * 306)/10 + (day - 62);
    }
}
