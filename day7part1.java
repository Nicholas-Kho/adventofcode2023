import java.io.IOException;
import java.nio.file.Files;
import java.nio.file.Path;
import java.nio.file.Paths;
import java.util.ArrayList;
import java.util.List;
import java.util.HashMap;
import java.util.Map;
import java.util.Set;
import java.util.stream.Collectors;
import java.util.TreeMap;
import java.util.LinkedHashMap;
import java.util.Collections;
import java.util.Comparator;

public class day7part1 {
    public static void main(String[] args) {
        String filePath = "src\\day7part1.txt";
        Path path = Paths.get(filePath);

        List<String> lines = new ArrayList<>();
        try {
            lines = Files.readAllLines(path);
        } catch (IOException e) {
            e.printStackTrace();
        }

        Map<String, ArrayList<String>> collection = new LinkedHashMap<>();
        collection.put("five of a kind", new ArrayList<>());
        collection.put("four of a kind", new ArrayList<>());
        collection.put("full house", new ArrayList<>());
        collection.put("three of a kind", new ArrayList<>());
        collection.put("two pair", new ArrayList<>());
        collection.put("one pair", new ArrayList<>());
        collection.put("high card", new ArrayList<>());

        Map<String, Integer> camelCards = new HashMap<>();

        for (String line: lines) {
            String[] splitLine = line.split(" ");
            Integer num = Integer.parseInt(splitLine[1]);
            camelCards.put(splitLine[0], num);
        }

        Set<String> keys = camelCards.keySet();

        for (String key: keys) {
            Map<String, Integer> usedChars = new HashMap<>();
            // c : 6
            // a : 1
            int uniqueChars = 0;

            int found = 1;
            for (int i = 0; i < key.length(); i++) {
                char now = key.charAt(i);
                String c = String.valueOf(now);
                if (usedChars.containsKey(c)) {
                    Integer previousValue = usedChars.get(c);
                    usedChars.put(c, previousValue + 1);
                    found += 1;
                } else {
                    usedChars.put(c, 1);
                }
            }
                        

            uniqueChars = 6-found;
            int jokers;

            int highestvalue = 0;
            String character = "";
            for (String key3 : usedChars.keySet()) {
                System.out.println(key3);
                if ((usedChars.get(key3) > highestvalue) && (String.valueOf(key3).equals("J") == false)) {
                    
                    if (key3 != "J") {
                        highestvalue = usedChars.get(key3);
                        character = key3;
                        // System.out.println(key3);
                    }
                    
                }
            }
            try { 
                jokers = usedChars.get("J");
                usedChars.put(character, highestvalue + jokers);
                usedChars.remove("J");
                if (jokers > 0 && jokers != 5) {
                uniqueChars -= 1;
            }
            }
            catch (IndexOutOfBoundsException e) {
                ;
            } catch (java.lang.NullPointerException e) {
                ;
            }
            
            System.out.println(uniqueChars);

            


            int singles = 0;
            int two_matches = 0;
            int three_matches = 0;

            if (three_matches != 0) {
                
            }

            Set<String> charKeys = usedChars.keySet();
            for (String cKey: charKeys) {
                // System.out.println(cKey + usedChars.get(cKey));
                switch (usedChars.get(cKey)) {
                    case 1 -> singles += 1;
                    case 2 -> two_matches += 1;
                    case 3 -> three_matches += 1;
                }
            }

            System.out.println(String.valueOf(usedChars) + String.valueOf(uniqueChars));
            if (uniqueChars == 5) {
                ArrayList<String> col = collection.get("high card");
                col.add(key);
                collection.put("high card", col);
            } else if (uniqueChars == 4) {
                ArrayList<String> col = collection.get("one pair");
                col.add(key);
                collection.put("one pair", col);
            } else if (uniqueChars == 3) {
                ArrayList<String> col;
                switch (three_matches) {
                    case 0:
                        col = collection.get("two pair");
                        col.add(key);
                        collection.put("two pair", col);
                        break;
                    case 1:
                        col = collection.get("three of a kind");
                        col.add(key);
                        collection.put("three of a kind", col);
                        break;
                }
            } else if (uniqueChars == 2) {
                ArrayList<String> col;
                switch (three_matches) {
                    case 1:
                        col = collection.get("full house");
                        col.add(key);
                        collection.put("full house", col);
                        break;
                    case 0:
                        col = collection.get("four of a kind");
                        col.add(key);
                        collection.put("four of a kind", col);
                        break;
                }
            } else if (uniqueChars == 1) {
                ArrayList<String> col = collection.get("five of a kind");
                col.add(key);
                collection.put("five of a kind", col);
            }
        
        }


        // int i = 0; i < key.length(); i++
        ArrayList<String> rankings = new ArrayList<>();



        for (String test: collection.keySet()) {
            List<String> temp = new ArrayList<>();
            for (String card: collection.get(test)) {
                temp.add(card);
                System.out.println(collection.get(test) + " " + test);
            }
            

            Collections.sort(temp, new CardComparator());
            for (int i = 0; i < temp.size(); i++) {
                rankings.add(temp.get(i));
                
            }
        }

        int winnings = 0;
        Collections.reverse(rankings);
        for (int y = 0; y < rankings.size(); y++) {
            // System.out.println(rankings.get(y)+ " " + (y + 1) + " " + camelCards.get(rankings.get(y)));
            winnings += (camelCards.get(rankings.get(y)) * (y + 1));
        }
        System.out.println(winnings);



        



    }


static class CardComparator implements Comparator<String> {
    @Override
    public int compare(String hand1, String hand2) {
        // Compare the lengths of the hands
        int lengthComparison = Integer.compare(hand2.length(), hand1.length());
        if (lengthComparison != 0) {
            return lengthComparison;
        }

        // If the lengths are the same, compare each card in the hands
        for (int i = 0; i < hand1.length(); i++) {
            char card1 = hand1.charAt(i);
            char card2 = hand2.charAt(i);

            // Use a strength map to determine the relative strength of each card
            Map<Character, Integer> strengthMap = new HashMap<>();
            for (int j = '2'; j <= '9'; j++) {
                strengthMap.put((char) j, j - '0');
            }
            strengthMap.put('T', 10);
            strengthMap.put('J', 1);
            strengthMap.put('Q', 11);
            strengthMap.put('K', 12);
            strengthMap.put('A', 13);

            int cardComparison = Integer.compare(strengthMap.getOrDefault(card2, 0), strengthMap.getOrDefault(card1, 0));
            if (cardComparison != 0) {
                return cardComparison;
            }
        }

        return 0; // Both hands are equal
    }
}
}