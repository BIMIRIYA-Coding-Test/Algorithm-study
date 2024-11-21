import java.util.*;

class Solution {
    boolean solution(String s) {
        Stack<Character> stack = new Stack<>();
        
        for (char c : s.toCharArray()) {
            if (c == '(') {
                stack.push(c);
            } else if (!stack.isEmpty()) {
                stack.pop(); 
            } else {
                return false;
            }
        }
        
        // 스택이 비어 있으면 true, 아니면 false
        return stack.isEmpty();
    }
}