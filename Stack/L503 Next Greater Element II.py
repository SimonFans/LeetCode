Given a circular array (the next element of the last element is the first element of the array), print the Next Greater Number for every element. The Next Greater Number of a number x is the first greater number to its traversing-order next in the array, which means you could search circularly to find its next greater number. If it doesn't exist, output -1 for this number.

Example 1:
Input: [1,2,1]
Output: [2,-1,2]
Explanation: The first 1's next greater number is 2; 
The number 2 can't find next greater number; 
The second 1's next greater number needs to search circularly, which is also 2.

class Solution:
    def nextGreaterElements(self, nums: List[int]) -> List[int]:
        # cycle so len(input)*2, and use mod % compute
        size=len(nums)
        ans=[-1]*size
        stack=[]
        for x in range(size*2):
            i=x%size
            while stack and nums[stack[-1]]<nums[i]:
                ans[stack.pop()]=nums[i]
            stack.append(i) # index
        return ans
