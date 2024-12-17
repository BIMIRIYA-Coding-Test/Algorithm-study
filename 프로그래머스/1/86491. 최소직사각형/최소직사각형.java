class Solution {
    public int solution(int[][] sizes) {
        int maxWidth = 0;  
        int maxHeight = 0; 
        
        
        for (int[] size : sizes) {
            int width = Math.max(size[0], size[1]);   // 큰 값을 가로로
            int height = Math.min(size[0], size[1]);  // 작은 값을 세로로
            
            // 가로, 세로 최댓값 갱신
            maxWidth = Math.max(maxWidth, width);
            maxHeight = Math.max(maxHeight, height);
        }
        
        return maxWidth * maxHeight;
    }
}