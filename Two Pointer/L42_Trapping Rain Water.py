Given n non-negative integers representing an elevation map where the width of each bar is 1, 
compute how much water it is able to trap after raining.

Example:

Input: [0,1,0,2,1,0,1,3,2,1,2,1]
Output: 6

# 双指针

class Solution:
    def trap(self, height: List[int]) -> int:
        l,r=0,len(height)-1
        left_height_max=0
        right_height_max=0
        ans=0
        while l<r:
            if height[l]<height[r]:
                left_height_max=max(left_height_max,height[l])
                ans+=left_height_max-height[l]
                l+=1
            else:
                right_height_max=max(right_height_max,height[r])
                ans+=right_height_max-height[r]
                r-=1
        return ans
        
        
        
