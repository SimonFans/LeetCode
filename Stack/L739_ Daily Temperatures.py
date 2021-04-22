'''
Given a list of daily temperatures T, return a list such that, for each day in the input, tells you how many days you would have to wait until a warmer temperature. If there is no future day for which this is possible, put 0 instead.

For example, given the list of temperatures T = [73, 74, 75, 71, 69, 72, 76, 73], your output should be [1, 1, 4, 2, 1, 1, 0, 0].

Note: The length of temperatures will be in the range [1, 30000]. Each temperature will be an integer in the range [30, 100]
'''


# Test case (General)

# Input: [73,74,75,71,69,72,76,73]
# Output: [1,1,4,2,1,1,0,0]


# Test case (Extra) 注意若input里面有相等数值的情况应该如何处理

# Input: [89,62,70,58,47,47,46,76,100,70]
# Output: [8,1,5,4,3,2,1,1,0,0]


# Solution <Stack>: 

class Solution:
    def dailyTemperatures(self, T: List[int]) -> List[int]:
        # result
        res = [0]*len(T)
        # stack
        stack = []
        
        for i in range(len(T) - 1, -1, -1):
            # do pop,stack里只记录右边比当前大的index
            while len(stack) != 0 and T[i] >= T[stack[-1]]:
                stack.pop()
            # Stack为空代表当前数字右侧没有比它大的，所以赋值0
            if len(stack) == 0:
                res[i] = 0
            # 计算两个index间的距离
            else:
                res[i] = stack[-1] - i
            stack.append(i)
        return res
      

  
  
