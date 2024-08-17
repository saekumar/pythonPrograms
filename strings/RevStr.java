package strings;
import java.util.*;
public class RevStr {
    public static void main(String[] args) {
        Scanner sc = new Scanner(System.in);

        String str = sc.nextLine();
        StringBuilder sb = new StringBuilder(str);
        System.out.println(sb.reverse());
        String revStr = "";
        for(int i=str.length()-1;i>=0;i--)
        {
            revStr+=str.charAt(i);
        }
        System.out.println(revStr);
        sc.close();
    }
}
