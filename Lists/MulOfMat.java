package Lists;

/**
 * MulOfMat
 */
import java.util.*;
public class MulOfMat {

    public static void main(String[] args) {
        int m1[][] = {{1,2,3},{4,5,6},{3,2,1}};
        int m2[][] = {{1,2,3},{4,5,6},{3,2,1}};

        matMul(m1,m2);
        
    }

    private static void matMul(int[][] m1, int[][] m2) {
      List<Integer> list = new ArrayList<>();
        for(int j=0;j<m1.length;j++)
        {
          int ar1[]= new int[m1.length];
          int ar2[] = new int[m1.length];
         for(int i=0;i<m1.length;i++)
         {

          ar1[i]  = m1[j][i];
          ar2[i] = m2[i][j];
         }
        list.add( mul(ar1,ar2));
          }

          for(int x:list)
          {
            System.out.println(x+" ");
          }
    }

    private static int  mul(int[] ar1, int[] ar2) {
        int tot = 0;

        for(int i=0;i<ar1.length;i++)
        {
            tot+=(ar1[i]*ar2[i]);
        }
        return tot;
    }
}