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

        Date emptyDate = new Date();
        Date myDate = new Date(11, 7, 1990);
        Date cloneDate = new Date(myDate);

        // Test Get operations
        Assert.assertEquals(emptyDate.getDay(), 1);
        Assert.assertEquals(emptyDate.getMonth(), 1);
        Assert.assertEquals(emptyDate.getYear(), 2000);

        // Test Get operations
        Assert.assertEquals(myDate.getDay(), 11);
        Assert.assertEquals(myDate.getMonth(), 7);
        Assert.assertEquals(myDate.getYear(), 1990);

        // Test clone
        Assert.assertTrue(myDate.equals(cloneDate));


        // Test Set operations
        myDate.set_day(12);
        myDate.set_month(8);
        myDate.set_year(1990);

        Assert.assertTrue(myDate.after(cloneDate));
        Assert.assertTrue(cloneDate.before(myDate));

        // Negative

        System.out.println("#-------- Completed Date tests");
    }

    private void testTrip() {

        Trip myTrip = new Trip("liam", 11, 7, 2017, 11, 8,
                2017, 3, 5);

        Trip cloneTrip = new Trip(myTrip);

        // Test Get operations
        Assert.assertTrue(myTrip.getGuideName().equals("liam"));
        Assert.assertTrue(myTrip.getDepartureDate().equals(new Date(11,7,2017)));
        Assert.assertTrue(myTrip.getReturningDate().equals(new Date(11, 8, 2017)));
        Assert.assertEquals(myTrip.getNoOfCountries(), 3);
        Assert.assertEquals(myTrip.getNoOfTravellers(), 5);

        // Test clone
        Assert.assertTrue(myTrip.equals(cloneTrip));


        // Test Set operations
        myTrip.set_guideName("Billy");
        Assert.assertTrue(myTrip.getGuideName().equals("Billy"));

        // Ops tests

        // Negative
        cloneTrip.set_departureDate(new Date(31, 2, 3000));
        Assert.assertEquals(cloneTrip.getDepartureDate(), myTrip.getDepartureDate());

        System.out.println("#-------- Completed Trip tests");
    }
}
