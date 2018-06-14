import com.sun.tools.javac.code.Attribute;

import java.io.*;
import java.lang.reflect.Array;
import java.util.*;
import java.util.Map.Entry;

public class Finder {

    private final static int PARAGRAPH_SIZE = 1000;

    private static HashMap<String, List<Integer>> namesAndLocations;
    private static String []  namesToSearch;


    private static void theMatcher(StringBuilder toSearch){
        // Iterate names
        for (String name: namesToSearch) {
            int fromIndex = 1;
            Integer nameIndex = toSearch.indexOf(name, fromIndex);
            ArrayList<Integer> offsetList = new ArrayList<Integer>();

            // Search text
            while (nameIndex > 0){
                offsetList.add(nameIndex);
                nameIndex = toSearch.indexOf(name, nameIndex + 1);
            }

            System.out.println("" + name + " --> " + offsetList.toString());

            // Adding to namesAndLocations
            if (namesAndLocations.get(name) == null) {
                namesAndLocations.put(name, offsetList);

            } else {
                namesAndLocations.get(name).addAll(offsetList);
            }
        }
    }

    private static void theAggregator(){
        for (Map.Entry<String, List<Integer>> entry : namesAndLocations.entrySet()) {
            System.out.println("Name = " + entry.getKey() + ", Offset = " + Arrays.toString(entry.getValue().toArray()));
        }
    }

    public static void main (String[] args) throws IOException {

//        String textFile = args[0];
//        String namesFile = args[1];
        String textFile = "/Users/liam/GitHub/liamsRepo/task/liamFinder/src/main/java/big.txt";
        String namesFile = "/Users/liam/Downloads/namesFile.txt";

        // Start reading text - lines start from 1
        LineNumberReader textReader = new LineNumberReader(new FileReader(textFile), 1);
        LineNumberReader namesReader = new LineNumberReader(new FileReader(namesFile), 1);

        // Initiate namesToSearch
        namesToSearch = namesReader.readLine().split(",");
        namesReader.close();
        System.out.println("Names: " + Arrays.toString(namesToSearch));

        // Initiate namesAndLocations
        namesAndLocations = new HashMap<String, List<Integer>>();
        for (String name: namesToSearch) {
            namesAndLocations.put(name, null);
        }

        // Start reading
        StringBuilder singleParagraph = new StringBuilder();

        while (textReader.ready()){
            // Collect lines till PARAGRAPH_SIZE
            String currLine = textReader.readLine();
            singleParagraph.append(currLine);

            if (textReader.getLineNumber() == PARAGRAPH_SIZE){
                theMatcher(singleParagraph);
            }
        }

        textReader.close();
        // Print results
        //theAggregator();
    }
}