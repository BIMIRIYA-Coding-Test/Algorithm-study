import java.util.*;
import java.util.stream.*;

class Solution {
    public String solution(int[] numbers) {
        List<String> numList = new ArrayList<>();
        
        for(int num : numbers){
            numList.add(String.valueOf(num));
        }
        
        numList.sort((a,b) -> (b+a).compareTo(a+b));
        
        if (numList.get(0).equals("0")) {
            return "0";
        }
        
        return numList.stream()
                      .collect(Collectors.joining());
    }
}