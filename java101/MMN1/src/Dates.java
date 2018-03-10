import java.util.Scanner;

public class Dates {

    public static void main(String [] args){

        final int MIN_MONTH = 1;
        final int MAX_MONTH = 12;
        final int MAX_NUM = 15;

        int maxDay = 31;

        int newYear;
        int newMonth;
        int newDay;

        Scanner scan = new Scanner(System.in);
        System.out.println("This program get a date and number of days and returns the final date");
        System.out.println("Please enter the year: ");
        int year = scan.nextInt();
        System.out.println("Please enter the month: ");
        int month = scan.nextInt();
        System.out.println("Please enter the day: ");
        int day = scan.nextInt();
        System.out.println("Please enter the number of days: ");
        int num = scan.nextInt();

        // Validate year is positive
        if ((year <= 0) || (month <= 0) || (day <= 0) || (num <= 0)){
            System.out.println("All digits must be positive!");
        } else {
            // Validate month is between 1 - 12
            if (month > MAX_MONTH){
                System.out.println("Month must be a value between 1 - 12");
            } else {
                // Get maxDay value
                if ((month == 4) || (month == 6) || (month == 9) || (month == 11)){
                    maxDay = 30;

                } else if (month == 2){
                    maxDay = 28;

                    if ((year % 4 == 0) || (year == 400)){
                        maxDay += 1;
                    }
                }
                // Validate day
                if (day > maxDay){
                    System.out.println("Month must be a value between 1 - 12");
                } else {
                    // Validate num
                    if (num > MAX_NUM) {
                        System.out.println("NUM must be a value between 1 - 15");
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
                        System.out.println("The original date is " + day + "/" + month + "/" + year + "\n" +
                                     "After " + num + " days the date is " + newDay + "/" + newMonth + "/" + newYear);
                    }
                }
            }
        }
    }
}
