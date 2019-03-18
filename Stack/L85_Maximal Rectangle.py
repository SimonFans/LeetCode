Given a 2D binary matrix filled with 0's and 1's, find the largest rectangle containing only 1's and return its area.

Input:
[
  ["1","0","1","0","0"],
  ["1","0","1","1","1"],
  ["1","1","1","1","1"],
  ["1","0","0","1","0"]
]
Output: 6

// L84 follow up, check L84

class Solution:
    def maximalRectangle(self, matrix: List[List[str]]) -> int:
        if not matrix or len(matrix)==0 or len(matrix[0])==0:
            return 0
        row=len(matrix)
        column=len(matrix[0])
        heights=[0]*column
        max_result=0
        for i in range(row):
            for j in range(column):
                if matrix[i][j]=='1':
                    heights[j]+=1
                else:
                    heights[j]=0
            area=self.largestRectangleArea(heights)
            max_result=max(max_result,area)
        return max_result
    
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
        
