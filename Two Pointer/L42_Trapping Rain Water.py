Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

class Solution:
    def trap(self, height: List[int]) -> int:
        # 双指针
        max_left,max_right,ans=0,0,0
        L, R=0, len(height)-1
        while L<R:
            if height[L]<=height[R]:
                max_left=max(max_left,height[L])
                ans+=max_left-height[L]
                L+=1
            else:
                max_right=max(max_right,height[R])
                ans+=max_right-height[R]
                R-=1
        return ans
        
        
        
