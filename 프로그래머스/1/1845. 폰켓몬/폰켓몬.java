import java.util.*;

class Solution {
    public int solution(int[] nums) {
        
        
        Set<Integer> setNums = new HashSet<>();
        
        for(int num : nums){
            setNums.add(num);
        }
        System.out.println(setNums.size());
        
        if(nums.length/2>setNums.size()){
            return setNums.size();
        }
        return nums.length/2;
    }
}