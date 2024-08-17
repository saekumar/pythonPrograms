
 package OOPS.Classes;
import java.util.*;
class Aeiou {
    public static void main(String[] args) {
        // Scanner sc = new Scanner(System.in);
        // char x = sc.next().charAt(0);
        
        
        
        //     if(x=='a' || x=='e' || x=='i' || x=='o' || x=='u')
        //     {
        //         System.out.println("Vowel");
        //     }
        //     else{
        //         System.out.print("Consonant");
        //     }
        //     System.out.println();
        //     sumOfDigits(2345);
            // displayOnlyChars();
            // lexicoGraphical();
            countAll();
        // sc.close();
    }



    private static void countAll() {
       String str = "Hello123!@# World456$";
       int charCount = str.length();
       int alphabetCount = str.replaceAll("[^a-zA-Z]", "").length();
       int digitCount = str.replaceAll("[^0-9]", "").length();
       int specialCount = str.replaceAll("[a-zA-Z0-9]", "").length();
       int wordCount = str.split(" ").length;

       System.out.println(charCount+" "+alphabetCount+" "+digitCount+" "+specialCount+" "+wordCount);

    }



    private static void lexicoGraphical() {
             String str = "HelloWorld".toLowerCase();
             char arr[] = str.toCharArray();
             Arrays.sort(arr);
             String res = "";
             for(char x:arr)
             {
                res+=x;
             }
             System.out.println(res);
    }



    private static void displayOnlyChars() {
        String str = "Hello123!@# World456$%^";
        String result = str.replaceAll("[^a-zA-Z0-9!-) ]", "");
        System.out.println(result);
    }



    private static void sumOfDigits(int n) {

        int sum = 0,c = 0;
        while (n>0) {
            sum+=(n%10);
            c++;
            n/=10;
            
        }
        System.out.println(sum+" "+c);
       
    }
  
    
}