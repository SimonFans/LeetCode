Implement next permutation, which rearranges numbers into the lexicographically next greater permutation of numbers.

If such arrangement is not possible, it must rearrange it as the lowest possible order (ie, sorted in ascending order).

The replacement must be in-place and use only constant extra memory.

Here are some examples. Inputs are in the left-hand column and its corresponding outputs are in the right-hand column.

1,2,3 → 1,3,2
3,2,1 → 1,2,3
1,1,5 → 1,5,1

#方法：从后往前找找第一个升序并且标记，不如14532， 找到4，然后和5换，换完后的序列进行reverse计算


class Solution(object):
    def nextPermutation(self, nums):
        """
        :type nums: List[int]
        :rtype: void Do not return anything, modify nums in-place instead.
        """
        
        p=-1
        for i in range(len(nums)-2,-1,-1):
            if nums[i]<nums[i+1]:
                p=i
                break
        if p==-1:
            nums.reverse()
            
        else:
            for j in range(len(nums)-1,p,-1):
                if nums[j]>nums[p]:
                    nums[j],nums[p]=nums[p],nums[j]
                    break
            left,right=p+1,len(nums)-1
        
            while left<right:
                nums[left],nums[right]=nums[right],nums[left]
                left+=1
                right-=1
                
                
                
