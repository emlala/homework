
import java.util.ArrayList;
import java.util.Scanner;

// A simple game that tries to guess the player's input.
// Game's over when either player or computer gets 25 points

public class MindReader {

    public static void main(String[] args) {
        Scanner reader = new Scanner(System.in);


        ArrayList<String> list = new ArrayList<>();
        int wins = 0;

        while (true) {
            if (wins >= 25 || list.size() - wins >= 25) {
                break;
            }

            String guessed = guess(list);

            System.out.print("Input h or t: ");
            String letter = reader.nextLine();
            if (!letter.equals("h") && !letter.equals("t")) {
                System.out.println("silly!");
                continue;
            }

            if (letter.equals(guessed)) {
                wins++;
            }
            list.add(letter);


            System.out.println("You input " + letter + ", I guessed " + guessed + ".");
            System.out.println("Computer's wins: " + wins);
            System.out.println("Player's wins: " + (list.size() - wins));

            System.out.println();
        }

        System.out.println("Game over.");
    }
    
    public static String guess(ArrayList<String> list) {
    
        if (list.size() < 3) {
            return "h";
        }
        
        String last = list.get(list.size() - 1);
        String penultimate = list.get(list.size() - 2);

        int index = 2;
        int h = 0;
        int t = 0;

        while (index < list.size()) {
            if (list.get(index - 2).equals(penultimate) && list.get(index - 1).equals(last)) {
                if (list.get(index).equals("h")) {
                    h++;
                } else {
                    t++;
                }
            }
            index++;
        }

        if (h > t) {
            return "h";
        } else {
            return "t";
        }
    }
}
