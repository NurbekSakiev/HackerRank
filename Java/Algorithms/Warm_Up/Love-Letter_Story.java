import java.io.*;
import java.util.*;
import java.text.*;
import java.math.*;
import java.util.regex.*;

public class Solution {

    public static void main(String[] args) {
        /* Enter your code here. Read input from STDIN. Print output to STDOUT. Your class should be named Solution. */
        Scanner scan = new Scanner(System.in);
        
        int numLines = scan.nextInt();
        for(int i = 0; i<numLines;i++) {
            int counter = 0;
            char[] chars = scan.next().toCharArray();
            int len = chars.length;
            int half = len/2;
            
            for (int j=0; j<half;j++) {
                if(chars[j]!=chars[len-j-1]) {
                    System.out.println(chars[j]-chars[len-j-1]);
                    counter+=Math.abs(chars[j]-chars[len-j-1]);
                }
            }
            System.out.println(counter);
        }
    }
}