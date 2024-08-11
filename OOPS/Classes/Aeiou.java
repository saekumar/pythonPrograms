
 package OOPS.Classes;
import java.util.*;
class Aeiou {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);
        String s = sc.nextLine();
        // shivaji ----> ['s','h','i','v','a','j','i']
        for(char x:s.toCharArray())
        {
            if(x=='a' || x=='e' || x=='i' || x=='o' || x=='u')
            {
                continue;
            }
            else{
                System.out.print(x+" ");
            }
        }
    }
  
    
}