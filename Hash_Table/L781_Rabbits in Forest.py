In a forest, each rabbit has some color. Some subset of rabbits (possibly all of them) tell you how many other rabbits have the same color as them. Those answers are placed in an array.

Return the minimum number of rabbits that could be in the forest.

Examples:
Input: answers = [1, 1, 2]
Output: 5
Explanation:
The two rabbits that answered "1" could both be the same color, say red.
The rabbit than answered "2" can't be red or the answers would be inconsistent.
Say the rabbit that answered "2" was blue.
Then there should be 2 other blue rabbits in the forest that didn't answer into the array.
The smallest possible number of rabbits in the forest is therefore 5: 3 that answered plus 2 that didn't.

Input: answers = [10, 10, 10]
Output: 11

Input: answers = []
Output: 0
Note:

answers will have length at most 1000.
Each answers[i] will be an integer in the range [0, 999].


"""
思路： 
1. 找山峰A[i]. 满足条件 A[i-1]<A[i] and A[i]>A[i+1]，即A[i]比它的左边和右边都大
2. 如果没有，返回0. 如果有，将A[i]左侧标为left, 右侧标为right.
3. 写两个while分别对left and right 进行讨论，目的是找到最左边和最右边
4. 计算left和right之间的最大距离


"""


class Solution:
    def longestMountain(self, A: List[int]) -> int:
        res=0
        for i in range(1,len(A)-1):
            if A[i-1]<A[i] and A[i]>A[i+1]:
                left,right=i-1,i+1
                while left>0 and A[left-1]<A[left]:
                    left-=1
                while right<len(A)-1 and A[right]>A[right+1]:
                    right+=1
                res=max(res,right-left+1)
        return res
        
        
        
