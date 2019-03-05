Given an array with n objects colored red, white or blue, sort them in-place so that objects of the same color are adjacent, with the colors in the order red, white and blue.

Here, we will use the integers 0, 1, and 2 to represent the color red, white, and blue respectively.

Note: You are not suppose to use the library's sort function for this problem.

Example:

Input: [2,0,2,1,1,0]
Output: [0,0,1,1,2,2]
Follow up:

A rather straight forward solution is a two-pass algorithm using counting sort.
First, iterate the array counting number of 0's, 1's, and 2's, then overwrite array with total number of 0's, then 1's and followed by 2's.
Could you come up with a one-pass algorithm using only constant space?

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Do not return anything, modify nums in-place instead.
        申请两枚指针，left 和 right，用 i 进行遍历，当 num[i] == 0时，交换当前位置和头指针处值，当 nums[i] == 2时，交换当前位置和尾指针处值，当 nums[i] == 1时，不进行交换
        """
        
        left, right = 0,len(nums)-1
        i=0
        while i<=right:
            if nums[i]==0:
                nums[left],nums[i]=nums[i],nums[left]
                left+=1
                i+=1
            elif nums[i]==1:
                i+=1
            else:
                nums[right],nums[i]=nums[i],nums[right]
                right-=1
