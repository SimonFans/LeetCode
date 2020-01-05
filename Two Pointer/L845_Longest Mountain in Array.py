Let's call any (contiguous) subarray B (of A) a mountain if the following properties hold:

B.length >= 3
There exists some 0 < i < B.length - 1 such that B[0] < B[1] < ... B[i-1] < B[i] > B[i+1] > ... > B[B.length - 1]
(Note that B could be any subarray of A, including the entire array A.)

Given an array A of integers, return the length of the longest mountain. 

Return 0 if there is no mountain.

Example 1:

Input: [2,1,4,7,3,2,5]
Output: 5
Explanation: The largest mountain is [1,4,7,3,2] which has length 5.
Example 2:

Input: [2,2,2]
Output: 0
Explanation: There is no mountain.
Note:

0 <= A.length <= 10000
0 <= A[i] <= 10000


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
        

