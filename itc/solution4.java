import java.io.*;
import java.math.*;
import java.security.*;
import java.text.*;
import java.util.*;
import java.util.concurrent.*;
import java.util.function.*;
import java.util.regex.*;
import java.util.stream.*;
import static java.util.stream.Collectors.joining;
import static java.util.stream.Collectors.toList;


class Result {

    /*
     * Complete the 'minSum' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts following parameters:
     *  1. INTEGER_ARRAY num
     *  2. INTEGER k
     */

    public static int minSum(List<Integer> num, int k) {
        PriorityQueue<Integer> heap = new PriorityQueue<Integer>(num.size(),Collections.reverseOrder());
        heap.addAll(num);
        for(int step=0; step<k;step++) {
            int value = heap.poll();
            int i = (int) Math.ceil((double) value / 2);
            heap.add(i);
        }
        return heap.stream().mapToInt(Integer::intValue).sum();
    }

}
public class Solution {