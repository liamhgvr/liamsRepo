import java.util.Scanner;

public class Milliseconds {

    public static void main (String [] args){

        final int SEC_IN_MINUTE = 60;
        final int SEC_IN_HOUR = 3600;
        final int SEC_IN_DAY = 86400;

        int d = 0;
        int h = 0;
        int m = 0;
        int s = 0;

        Scanner scan = new Scanner(System.in);
        System.out.println("This program reads an integer which represents milliseconds and converts it to days," +
                " hours, minuts and seconds.");
        System.out.println("Please enter the number of milliseconds: ");
        long ms = scan.nextLong();

        int inSeconds = (int) ms / 1000;

        while (inSeconds > 0) {

            if (inSeconds >= SEC_IN_DAY) {
                d = inSeconds / SEC_IN_DAY;
                inSeconds = inSeconds - (d * SEC_IN_DAY);

            } else if (inSeconds >= SEC_IN_HOUR) {
                h = inSeconds / SEC_IN_HOUR;
                inSeconds = inSeconds - (h * SEC_IN_HOUR);

            } else if (inSeconds >= SEC_IN_MINUTE) {
                m = inSeconds / SEC_IN_MINUTE;
                inSeconds = inSeconds - (m * SEC_IN_MINUTE);

            } else {
                s = inSeconds;
                inSeconds = 0;
            }
        }
        System.out.println("Day: " + d + " hour: " + h + " minutes: " + m + " seconds: " + s + "");
    } // end of main
} // end of class milliseconds