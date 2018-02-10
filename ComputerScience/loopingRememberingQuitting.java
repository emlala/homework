
import java.util.Scanner;

public class LoopingRememberingQuitting {

    public static void main(String[] args) {

        Scanner reader = new Scanner(System.in);
        
        int sum = 0;
        int count = 0;
        int evens = 0;
        int odds = 0;
        
        System.out.println("Insert numbers:");
        while (true) {
            int number = Integer.parseInt(reader.nextLine());
            
            if (number == -1) {
                System.out.println("Thank you and goodbye!");
                System.out.println("Sum: " + sum);
                System.out.println("How many numbers? " + count);
                System.out.println("Average: " + (double) sum / count);
                System.out.println("Even numbers: " + evens);
                System.out.println("Odd numbers: " + odds);
                break;
            }
            
            if (number % 2 == 0) {
                evens++;
            } else {
                odds++;
            }
            
            
            sum += number;
            count++;
        }
    }
}
