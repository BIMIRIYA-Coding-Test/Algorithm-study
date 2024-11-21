import java.util.*;

public class Solution {
    public int[] solution(int[] arr) {
        List<Integer> answer = new ArrayList<>();
        
        // 이전 값을 저장하기 위한 변수 초기화
        int prev = -1; 
        
        for (int num : arr) {
            // 이전 값과 같지 않으면 리스트에 숫자 추가
            if (num != prev) {
                answer.add(num);
                prev = num;
            }
        }
        
        // List를 int 배열로 변환하여 반환
        return answer.stream().mapToInt(Integer::intValue).toArray();
    }
}