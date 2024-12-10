import java.util.*;

class Solution {
    public int solution(int[] nums) {
        
        
        Set<Integer> setNums = new HashSet<>();
        
        for(int num : nums){
            setNums.add(num);
        }
        System.out.println(setNums.size());
        
        return Integer.min(nums.length/2, setNums.size());
    }
}