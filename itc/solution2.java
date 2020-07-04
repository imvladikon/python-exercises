import java.io.*;
import java.util.*;
import java.util.regex.*;


import java.io.IOException;
import java.nio.charset.StandardCharsets;
import java.nio.file.*;
import java.util.List;
import java.util.Map;
import java.util.function.Function;
import java.util.stream.*;
import static java.util.function.Function.identity;
import static java.util.stream.Collectors.*;


import static java.util.Arrays.asList;

public class Solution {
    private static final Scanner scan = new Scanner(System.in);
    
    public static String getFileExtension(String fileName) {
        String extension = "";
        int i = fileName.lastIndexOf('.');
        if (i >= 0) {
            extension = fileName.substring(i+1);
        }
        return extension;
    }

    public static void main(String args[]) throws Exception {
        // read the string filename
        String baseFilename;
        baseFilename = scan.nextLine();
       Function<String, String> GET_NAME_FILE = str -> getFileExtension(str) + "_" + baseFilename;
        Map<String, List<String>> emptyMap = Stream.of(GET_NAME_FILE.apply(".cs"),
                GET_NAME_FILE.apply(".cpp"),
                GET_NAME_FILE.apply(".c"))
                .collect(toMap(identity(), f -> new ArrayList<>()));
        try (Stream<String> stream = Files.lines(Paths.get(baseFilename))) {

            Map<String, List<String>> map = stream.filter(s -> !s.isEmpty())
                    .collect(Collectors.groupingBy(GET_NAME_FILE, () -> emptyMap, toList()));

            map.forEach((k,v)-> {
                try {
                    Files.write(Paths.get(k),v, StandardCharsets.UTF_8);
                } catch (IOException e) {
                    e.printStackTrace();
                }
            });

        } catch (IOException e) {
            e.printStackTrace();
        }
        
    }