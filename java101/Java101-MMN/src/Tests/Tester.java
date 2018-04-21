package Tests;

import MMN12.Date;
import MMN12.Trip;
import MMN13.javaTours;
import common.validations;
import org.junit.Assert;


public class Tester extends validations{

    public static void main(String[] args) {

        Tester t = new Tester();

        t.testValidations();
        t.testDate();
        t.testTrip();
//        t.testJavaTours();
    }

    private void testValidations(){
        System.out.println("#----- Started Valid Tests");

        // Valid Dates
        Assert.assertTrue(isValidDate(1, 1, 2018));
        Assert.assertTrue(isValidDate(31, 12, 2100));
        Assert.assertTrue(isValidDate(30, 9, 2025));
        Assert.assertTrue(isValidDate(28, 2, 2025));
        Assert.assertTrue(isValidDate(29, 2, 2100));

        // Invalid Dates
        Assert.assertFalse(isValidDate(0, 1, 2018));
        Assert.assertFalse(isValidDate(1, 1, 2101));
        Assert.assertFalse(isValidDate(31, 9, 2025));
        Assert.assertFalse(isValidDate(29, 2, 2025));
        Assert.assertFalse(isValidDate(30, 2, 2100));
        System.out.println("#----- Completed Valid Tests");
    }

    private void testDate() {

        Date emptyDate = new Date();
        Date testDate = new Date(11, 7, 2018);
        Date cloneDate = new Date(testDate);

        System.out.println("#----- Started Date Tests");

        // Default Tests
        Assert.assertEquals(emptyDate.getDay(), 1);
        Assert.assertEquals(emptyDate.getMonth(), 1);
        Assert.assertEquals(emptyDate.getYear(), 1990);

        // Test Get operations
        Assert.assertEquals(testDate.getDay(), 11);
        Assert.assertEquals(testDate.getMonth(), 7);
        Assert.assertEquals(testDate.getYear(), 2018);

        // Test clone
        Assert.assertTrue(testDate.equals(cloneDate));
        Assert.assertEquals(cloneDate.getDay(), 11);
        Assert.assertEquals(cloneDate.getMonth(), 7);
        Assert.assertEquals(cloneDate.getYear(), 2018);
        
        // Test Set operations
        testDate.set_day(12); testDate.set_month(8); testDate.set_year(2019);
        Assert.assertEquals(testDate.getDay(), 12);
        Assert.assertEquals(testDate.getMonth(), 8);
        Assert.assertEquals(testDate.getYear(), 2019);
        
        // Methods Test
        Assert.assertTrue(testDate.after(cloneDate));
        Assert.assertTrue(cloneDate.before(testDate));
        Assert.assertEquals(testDate.difference(cloneDate), 397);

        // Test negative assignment
        cloneDate = new Date(testDate);
        testDate.set_day(41); testDate.set_month(13); testDate.set_year(1880);
        Assert.assertTrue(testDate.equals(cloneDate));

        System.out.println("#----- Completed Date Tests");
    }

    private void testTrip() {

        Trip testTrip = new Trip("liam", 11, 7, 2017, 11, 8,
                2017, 3, 5);
        Trip cloneTrip = new Trip(testTrip);

        System.out.println("#----- Started Trip Tests");

        // Test Get operations
        Assert.assertTrue(testTrip.getGuideName().equals("liam"));
        Assert.assertTrue(testTrip.getDepartureDate().equals(new Date(11, 7, 2017)));
        Assert.assertTrue(testTrip.getReturningDate().equals(new Date(11, 8, 2017)));
        Assert.assertEquals(testTrip.getNoOfCountries(), 3);
        Assert.assertEquals(testTrip.getNoOfTravellers(), 5);

        // Test clone
        Assert.assertTrue(testTrip.equals(cloneTrip));
        Assert.assertTrue(cloneTrip.equals(testTrip));
        Assert.assertTrue(cloneTrip.getGuideName().equals("liam"));
        Assert.assertTrue(cloneTrip.getDepartureDate().equals(new Date(11, 7, 2017)));
        Assert.assertTrue(cloneTrip.getReturningDate().equals(new Date(11, 12, 2017)));
        Assert.assertEquals(cloneTrip.getNoOfCountries(), 3);
        Assert.assertEquals(cloneTrip.getNoOfTravellers(), 5);

        // Test Set operations
        String testName = "Billy";
        testTrip.set_guideName(testName);
        Assert.assertTrue(testTrip.getGuideName().equals(testName));

        Date testTripDate = new Date(5, 11, 2017);
        testTrip.set_departureDate(testTripDate);
        Assert.assertTrue(testTrip.getDepartureDate().equals(testTripDate));

        testTripDate.set_day(15);
        testTripDate.set_month(9);
        testTripDate.set_year(2025);
        testTrip.set_returningDate(testTripDate);
        Assert.assertTrue(testTrip.getReturningDate().equals(testTripDate));

        int testNoOfCountries = 8;
        testTrip.set_noOfCountries(testNoOfCountries);
        Assert.assertEquals(testTrip.getNoOfCountries(), testNoOfCountries);

        int testNoOfTravellers = 20;
        testTrip.set_noOfTravellers(testNoOfTravellers);
        Assert.assertEquals(testTrip.getNoOfTravellers(), testNoOfTravellers);

        // Negative
        Date defaultDate = new Date();
        cloneTrip.set_departureDate(new Date(31, 2, 3000));
        Assert.assertTrue(cloneTrip.getDepartureDate().equals(defaultDate));

        System.out.println("#----- Completed Trip tests");
    }

    private void testJavaTours() {

        Date testDate = new Date(11,7,2018);
        Trip firstTrip = new Trip("liam", 11, 7, 2018, 11, 8,2018, 3, 5);
        Trip secondTrip = new Trip("mike", 22, 5, 2017, 23, 5,2017, 4, 6);
        Trip thirdTrip = new Trip("liam", 22, 5, 2017, 23, 5,2017, 10, 10);

        javaTours testTours = new javaTours();

        System.out.println("#----- Started JavaTours Tests");

        // Null tests
        Assert.assertTrue(testTours.getNoOfTrips() == 0);
        Assert.assertTrue(!testTours.removeTrip(firstTrip));
        Assert.assertTrue(testTours.howManyTravellers() == 0);
        Assert.assertTrue(testTours.howManyTripDepartures(testDate) == 0);
        Assert.assertTrue(testTours.howManyCars(testDate) == 0);
        Assert.assertTrue(testTours.longestTrip() == null);
        Assert.assertTrue(testTours.mostPopularGuide() == null);
        Assert.assertTrue(testTours.earliestTrip() == null);
        Assert.assertTrue(testTours.mostExpensiveTrip() == null);

        // Add trip test
        Assert.assertTrue(testTours.addTrip(firstTrip));
        Assert.assertTrue(testTours.addTrip(secondTrip));
        Assert.assertTrue(testTours.addTrip(thirdTrip));

        // Get and Stat methods
        Assert.assertEquals(testTours.getNoOfTrips(), 3);
        Assert.assertEquals(testTours.howManyTravellers(), 11);
        Assert.assertEquals(testTours.howManyTripDepartures(testDate), 1);
        Assert.assertEquals(testTours.howManyCars(testDate),1);
        Assert.assertTrue(testTours.longestTrip().equals(secondTrip));
        Assert.assertTrue(testTours.mostPopularGuide().equals("liam"));
        Assert.assertTrue(testTours.earliestTrip().equals(secondTrip));
        Assert.assertTrue(testTours.mostExpensiveTrip().equals(secondTrip));

        System.out.println("#----- Completed JavaTours Tests");
    }
}
