package MMN11;

import java.util.Scanner;

public class Dates {

    public static void main(String[] args) {

        final int MIN_MONTH = 1;
        final int MAX_MONTH = 12;
        final int MAX_NUM = 10;

        final int FEB = 2;
        final int APR = 4;
        final int JUN = 6;
        final int SEP = 9;
        final int NOV = 11;

        int maxDay = 31;

        int newYear;
        int newMonth;
        int newDay;

        // Getting initial date
        Scanner scan = new Scanner(System.in);
        System.out.println("This program get a date and number of days and returns the final date. \n" +
                "Please enter a valid date (year month day)");
        int year = scan.nextInt();
        int month = scan.nextInt();
        int day = scan.nextInt();

        // Validate Month corners
        if (month == FEB) {
            if ((year % 4 == 0) || (year == 400)) {
                maxDay = 29;
            } else {
                maxDay = 28;
            }
        } else if ((month == APR) || (month == JUN) || (month == SEP) || (month == NOV)) {
            maxDay = 30;
        }


        // Validate year is positive
        if ((year <= 0) || (month <= 0) || (day <= 0)) {
            System.out.println("All digits must be positive!");
        } else if (month > MAX_MONTH) {
            System.out.println("The original date is invalid!");
        } else if (day > maxDay) {
            System.out.println("The original date is invalid!");
        } else {

            // Getting number of days to calculate
            System.out.println("Please enter the number of days (1 - 15): ");
            int num = scan.nextInt();

            if (num > MAX_NUM || num < 0) {
                System.out.println("Please enter the number of days (0 - 10): ");
            } else {
                // Calculate
                newYear = year;
                newMonth = month;
                newDay = day + num;

                if (newDay + num > maxDay) {

                    newDay = newDay - maxDay;
                    newMonth += 1;

                    if (newMonth > MAX_MONTH) {

                        newMonth = MIN_MONTH;
                        newYear += 1;
                    }
                }
                // Print results
                System.out.println("The original date was: " + day + "/" + month + "/" + year + "\n" +
                        "After " + num + " days the date is: " + newDay + "/" + newMonth + "/" + newYear);
            }
        }
    } // end of main
} // end of class dates
