import java.util.*;

class Solution {
    public List<Integer> solution(int[] progresses, int[] speeds) {
        Queue<Integer> daysQueue = new LinkedList<>();
        
        // 각 작업의 완료 일수를 Queue에 추가
        for (int i = 0; i < speeds.length; i++) {
            int remainingDays = (100 - progresses[i] + speeds[i] - 1) / speeds[i];
            daysQueue.add(remainingDays);
        }
        
        List<Integer> result = new ArrayList<>();
        
        while (!daysQueue.isEmpty()) {
            int count = 1;
            int current = daysQueue.poll();
            
            // 같은 배포 그룹에 포함되는 작업을 처리
            while (!daysQueue.isEmpty() && daysQueue.peek() <= current) {
                daysQueue.poll();
                count++;
            }
            
            result.add(count);
        }
        
        return result;
    }
}
