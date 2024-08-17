package OOPS.Classes;
import java.util.*;

public class Occurence {
    public static void main(String[] args) {
        Scanner scc = new Scanner(System.in);
        String str = scc.nextLine();

        // check(str);
        check2(str);
    }

    private static void check2(String str) {
     Map<String,Integer> hash = new HashMap<>();
     for(String x:str.split(" "))
     {
        hash.put(x, hash.getOrDefault(x, 0)+1);
     }

     for(String s:hash.keySet())
     {
        System.out.println(s+" "+hash.get(s));

     }



    }

    private static void check(String str) {
        ArrayList<Item> list = new ArrayList<>();
        String arr[] = str.split(" ");
        
        for (int i = 0; i < arr.length; i++) {
            String st = arr[i];
            Item item = new Item(st, 1);
            if (list.contains(item)) {
                int index = list.indexOf(item);
                Item it = list.get(index);
                it.occu++;
                list.set(index, it);
            } else {
                list.add(item);
            }
        }

        for (Item i : list) {
            System.out.println(i.s + " " + i.occu);
        }
    }
}

class Item {
    String s;
    int occu;

    Item(String s, int occu) {
        this.s = s;
        this.occu = occu;
    }

    @Override
    public boolean equals(Object o) {
        if (this == o) return true;
        if (o == null || getClass() != o.getClass()) return false;
        Item item = (Item) o;
        return Objects.equals(s, item.s);
    }

    @Override
    public int hashCode() {
        return Objects.hash(s);
    }
}
