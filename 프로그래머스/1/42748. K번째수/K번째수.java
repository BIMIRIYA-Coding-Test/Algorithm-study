import java.util.*;

class Solution {
   public int[] solution(int[] array, int[][] commands) {
        int[] result = new int[commands.length];
        
        for (int idx = 0; idx < commands.length; idx++) {
            int i = commands[idx][0];
            int j = commands[idx][1];
            int k = commands[idx][2];
            
            List<Integer> subList = new ArrayList<>();
            for (int x = i - 1; x < j; x++) {
                subList.add(array[x]);
            }
            // 정렬
            Collections.sort(subList);
            
            // k번째 수 추출
            result[idx] = subList.get(k - 1);
        }
        
        return result;
    }
}