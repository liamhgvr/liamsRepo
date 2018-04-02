package Tests;

import MMN12.Date;
import MMN12.Trip;
import org.junit.Assert;

public class Tester {

    public static void main(String[] args) {

        Tester t = new Tester();

        t.testDate();
        t.testTrip();
    }

    private void testDate() {

        int testYear = 2018;
        int testMonth = 7;
        int testDay = 11;

        Date emptyDate = new Date();
        Date myDate = new Date(testDay, testMonth, testYear);
        Date newDate = new Date(myDate);

        Assert.assertEquals(myDate.getDay(), testDay);
        Assert.assertEquals(emptyDate.getDay(), 1);
        Assert.assertEquals(newDate.getMonth(), 7);
    }

    private void testTrip() {

        String testGuide = "liam";
        int testDepDay = 11;

        Trip t = new Trip("liam", 11, 7, 2017, 11, 8, 2017, 3, 5);

        System.out.println(t.getGuideName());
        System.out.println(t.getDepartureDate());
        System.out.println(t.getReturningDate());
        System.out.println(t.getNoOfCountries());
        System.out.println(t.getNoOfTravellers());

        System.out.println(t.calculatePrice());
    }
}
