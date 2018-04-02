public class Date extends MMN11.dates{

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
        _day = day;
        _month = month;
        _year = year;
    }

    public Date(Date other){
        Date date = other;
    }

    // methods

}
