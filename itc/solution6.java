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
     * Complete the 'largestMatrix' function below.
     *
     * The function is expected to return an INTEGER.
     * The function accepts 2D_INTEGER_ARRAY arr as parameter.
     */

    public static int largestMatrix(List<List<Integer>> arr) {
        //using dynamic programming with dp matrix for subtask and backtracking
        int rows = arr.size();
        int columns = arr.get(0).size();
        int[][] dp = new int[rows][columns];
        for (int i = 0; i < rows; i++) {
            dp[i][0] = arr.get(0).get(i);
        }
        for (int j = 0; j < columns; j++) {
            dp[0][j] = arr.get(j).get(0);
        }
        for (int i = 1; i < rows; i++) {
            for (int j = 1; j < columns; j++) {
                if (arr.get(j).get(i) == 1) {
                    dp[i][j] = Math.min(dp[i][j - 1],
                            Math.min(dp[i - 1][j], dp[i - 1][j - 1])) + 1;
                } else {
                    dp[i][j] = 0;
                }
            }
        }
        int result = dp[0][0];
        for (int i = 0; i < rows; i++) {
            for (int j = 0; j < columns; j++) {
                if (result < dp[i][j]) {
                    result = dp[i][j];
                }
            }
        }
        return result;

    }

}
public class Solution {