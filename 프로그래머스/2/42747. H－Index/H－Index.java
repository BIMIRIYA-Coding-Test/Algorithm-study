import java.util.*;

class Solution {
    public int solution(int[] citations) {
        Arrays.sort(citations); 
        int n = citations.length;

        
        int hIndex = 0;
        for (int i = 0; i < n; i++) {
            
            if (citations[i] >= n - i) {
                hIndex = n - i;
                break;
            }
        }
        return hIndex;
    }
}