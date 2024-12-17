import java.util.*;

class Solution {
    public int solution(String[][] clothes) {
        HashMap<String, Integer> clothingMap = new HashMap<>();
        
        for (String[] cloth : clothes) {
            String type = cloth[1];
            clothingMap.put(type, clothingMap.getOrDefault(type, 0) + 1);
        }
        
        int combinations = 1;
        for (int count : clothingMap.values()) {
            combinations *= (count + 1); 
        }
        
        return combinations - 1;
    }
}