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



import java.math.RoundingMode;
import java.text.DecimalFormat;
import java.text.DecimalFormatSymbols;
import java.text.NumberFormat;
import java.util.Collections;
import java.util.List;

class Result {

    private final static boolean IS_DEBUG_MODE = false; 
    /*
     * Complete the 'interpolate' function below.
     *
     * The function is expected to return a STRING.
     * The function accepts following parameters:
     *  1. INTEGER n
     *  2. INTEGER_ARRAY instances
     *  3. FLOAT_ARRAY price
     */

    public static String interpolate(int n, List<Integer> instances0, List<Float> price0) {
        // System.out.println(Arrays.toString(instances0.toArray()));
        // System.out.println(n);
        // System.out.println(Arrays.toString(price0.toArray()));
        float result;
        List<Integer> instances = new ArrayList<>();
        List<Float> price = new ArrayList<>();
        for (int i = 0; i<price0.size();i++) {
            if(price0.get(i)<=0) {
                continue;
            }
            instances.add(instances0.get(i));
            price.add(price0.get(i));
        }
        if(price.size() == 1) {
            return buildNumberFormat(2).format(price.get(0));
        }
        Integer last_point = instances.get(instances.size() - 1);
        Integer first_point = instances.get(0);
        if (n== last_point) {
            return buildNumberFormat(2).format(price.get(price.size()-1));
        }
        if (n== first_point) {
            return buildNumberFormat(2).format(price.get(0));
        }
        if (n > last_point) {
            result = findBylinInterpolation(n, instances.get(instances.size() - 2), last_point, price.get(price.size() - 2), price.get(price.size() - 1));
            return buildNumberFormat(2).format(result);
        }
        if (n < first_point) {
            result = findBylinInterpolation(n, instances.get(1), first_point, price.get(1), price.get(0));
            return buildNumberFormat(2).format(result);
        }
        int idx = 0;
        for (int i = 0; i<instances.size();i++) {
            if (n<instances.get(i)) {
                idx = i;
                break;
            }
        }
        result = findBylinInterpolation(n, instances.get(idx - 1), instances.get(idx), price.get(idx - 1), price.get(idx));
        return buildNumberFormat(2).format(result);
    }
    public static float findBylinInterpolation(int n, int x1, int x2, float y1, float y2) {
        float a = (y2-y1)/(x2-x1);
        float b = y1 - x1*(y2-y1)/(x2-x1);
        return a*n+b;
    }

     public static DecimalFormatSymbols makeDecimalFormatSymbols() {
        DecimalFormatSymbols decimalFormatSymbols = new DecimalFormatSymbols();
        decimalFormatSymbols.setDecimalSeparator('.');
        decimalFormatSymbols.setGroupingSeparator(' ');
        return decimalFormatSymbols;
    }

    public static NumberFormat buildNumberFormat(int digitsAfterComma) {
        NumberFormat result = new DecimalFormat("###,###.##", makeDecimalFormatSymbols());
        result.setMinimumFractionDigits(0);
        result.setMaximumFractionDigits(digitsAfterComma);
        result.setRoundingMode(RoundingMode.HALF_UP);
        result.setGroupingUsed(false);
        return result;
    }

}
public class Solution {