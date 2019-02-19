Given an integer array, find three numbers whose product is maximum and output the maximum product.

Example 1:

Input: [1,2,3]
Output: 6
 

Example 2:

Input: [1,2,3,4]
Output: 24


class Solution:
    def maximumProduct(self, nums: 'List[int]') -> 'int':
        nums.sort()
        
        n=len(nums)
        # [-3,-2,-1,0]
        if nums[n-1]==0:
            return 0
        
        product=1
        # [-4,-3,-2,-1]
        if nums[n-1]<=0:
            for i in range(n-1,n-3-1,-1):
                product*=nums[i]
            return product
        else:
            # index
            i=0
            j=n-1
        
            product*=nums[n-1]
            j-=1
            k=3-1
        
            k//=2
            for i in range(k):
                left_max=nums[i]*nums[i+1]
                right_max=nums[j]*nums[j-1]
                if left_max>right_max:
                    product*=left_max
                    i+=2
                else:
                    product*=right_max
                    j-=2
        return product
        
        
