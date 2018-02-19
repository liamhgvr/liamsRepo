import java.util.Scanner;

public class Milliseconds {

    public static void main (String [] args){

        final int SEC_IN_MINUTE = 60;
        final int SEC_IN_HOUR = 3600;
        final int SEC_IN_DAY = 86400;

        long d = 0;
        long h = 0;
        long m = 0;
        long s = 0;

        int t = 100 / SEC_IN_MINUTE;
        System.out.println(t);

        Scanner scan = new Scanner(System.in);
        System.out.println("This program reads an integer which represents milliseconds and converts it to days," +
                " hours, minuts and seconds.");
        System.out.println("Please enter the number of milliseconds: ");
        // long ms = scan.nextLong();
        long ms = 100000;

        long inSeconds = ms / 1000;

        while (inSeconds > 0) {
            if (inSeconds >= SEC_IN_DAY) {
                d = ms / SEC_IN_DAY;
                inSeconds = inSeconds - (d * SEC_IN_DAY);
                System.out.println(ms);

            } else if (inSeconds >= SEC_IN_HOUR) {
                h = ms / SEC_IN_HOUR;
                inSeconds = inSeconds - (h * SEC_IN_HOUR);
                System.out.println(ms);

            } else if (inSeconds >= SEC_IN_MINUTE) {
                m = ms / SEC_IN_MINUTE;
                inSeconds = inSeconds - (m * SEC_IN_MINUTE);
                System.out.println(ms);
            } else {
                s = inSeconds;
                inSeconds = 0;
            }
        }
        System.out.println("Day: " + d + " hour: " + h + " minutes: " + m + " seconds: " + s + "");
        //System.out.println(inSeconds);

    } // end of main
} // end of class milliseconds
