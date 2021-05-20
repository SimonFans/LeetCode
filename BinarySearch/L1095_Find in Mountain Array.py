'''
(This problem is an interactive problem.)

You may recall that an array A is a mountain array if and only if:

A.length >= 3
There exists some i with 0 < i < A.length - 1 such that:
A[0] < A[1] < ... A[i-1] < A[i]
A[i] > A[i+1] > ... > A[A.length - 1]
Given a mountain array mountainArr, return the minimum index such that mountainArr.get(index) == target.  If such an index doesn't exist, return -1.

You can't access the mountain array directly.  You may only access the array using a MountainArray interface:

MountainArray.get(k) returns the element of the array at index k (0-indexed).
MountainArray.length() returns the length of the array.
Submissions making more than 100 calls to MountainArray.get will be judged Wrong Answer.  Also, any solutions that attempt to circumvent the judge will result in disqualification.

Input: array = [1,2,3,4,5,3,1], target = 3
Output: 2
Explanation: 3 exists in the array, at index=2 and index=5. Return the minimum index, which is 2.

Input: array = [0,1,2,4,2,1], target = 3
Output: -1
Explanation: 3 does not exist in the array, so we return -1.

'''

Solution:
  
# """
# This is MountainArray's API interface.
# You should not implement it, or speculate about its implementation
# """
#class MountainArray:
#    def get(self, index: int) -> int:
#    def length(self) -> int:

# Binary Search

class Solution:
    def findInMountainArray(self, target: int, mountain_arr: 'MountainArray') -> int:
        arr_len = mountain_arr.length()
        left, right = 0, arr_len - 1
        while left <= right:
            mid = left + (right - left)//2
            #如果左边比右边大，不确定左边的左边是否有更大的，所以应该继续寻找左边的左边
            if mountain_arr.get(mid) >= mountain_arr.get(mid+1):
                right = mid - 1
            else:
                left = mid + 1
        peak = left
        if mountain_arr.get(peak) == target:
            return peak
        
        # [ 1 2 3 4 5 3 1 ] 
        # 以peak为点，先搜索peak前面的
        left, right = 0, peak-1 
        while left <= right:
            mid = left + (right - left)//2
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) > target:
                right = mid -1
            else:
                left = mid + 1
                
        # 以peak为点，搜索peak后面的
        left, right = peak + 1, arr_len - 1
        while left <= right:
            mid = left + (right - left)//2
            if mountain_arr.get(mid) == target:
                return mid
            elif mountain_arr.get(mid) > target:
                left = mid + 1
            else:
                right  = mid -1
        return -1
