import java.io.*;
import java.util.HashMap;
import java.util.List;
import java.util.Scanner;
import java.util.regex.Matcher;
import java.util.regex.Pattern;

public class Finder {

    private final static int MAX_LINES = 10;
    private static HashMap namesAndLocations;

    private static String [] namesToSearch;
    private static String [] currParagraph;


    public static void theMatcher(StringBuilder stringToSearch){
        //String[][] offsetLists = new String[][];
        int index = 0;
        int charOffset;
        namesToSearch = new String[10];
        namesToSearch[0] = "The";
        namesToSearch[1] = "laws";

        System.out.println(stringToSearch.length());

        while (index < stringToSearch.length()){
            charOffset = stringToSearch.indexOf(namesToSearch[0]);
            System.out.println(stringToSearch.indexOf(namesToSearch[0], index));
            index = charOffset + namesToSearch[0].length();
        }
        System.out.println(stringToSearch);
    }

    public static void theAggregator(){}

    public static void main (String[] args) throws IOException {

//        String textFile = args[0];
//        String namesFile = args[1];
        String textFile = "/Users/liam/GitHub/liamsRepo/task/liamFinder/src/main/java/big.txt";
        String namesFile = "/Users/liam/GitHub/liamsRepo/task/liamFinder/src/main/java/testText.txt";

        LineNumberReader reader = new LineNumberReader(new FileReader(textFile));
        StringBuilder sb = new StringBuilder();

        try {
            String line = reader.readLine();

            while (line != null) {
                System.out.println(line);
                sb.append(line);
                if (reader.getLineNumber() == MAX_LINES){

                    // Insert Matcher
                    theMatcher(sb);

                    break;
                }
                line = reader.readLine();
            }
                // Insert Aggregator
        } catch (IOException e) {
            e.printStackTrace();
        } finally {
            try {
                reader.close();
            } catch (IOException e) {
                e.printStackTrace();
            }
        }
    }
}