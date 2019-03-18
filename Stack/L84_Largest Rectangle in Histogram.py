Given n non-negative integers representing the histogram's bar height where the width of each bar is 1,
find the area of largest rectangle in the histogram.

Above is a histogram where width of each bar is 1, given height = [2,1,5,6,2,3].
The largest rectangle is shown in the shaded area, which has area = 10 unit

class Solution:
    def largestRectangleArea(self, heights: List[int]) -> int:
        res=0
        stack=[]
        heights.append(0)
        N=len(heights)
        for i in range(N):
            if not stack or heights[i]>heights[stack[-1]]:
                stack.append(i)
            else:
                while stack and heights[i]<=heights[stack[-1]]:
                    h=heights[stack[-1]]
                    stack.pop()
                    w=i if not stack else i-stack[-1]-1
                    res=max(res,w*h)
                stack.append(i)
        return res
        
        
