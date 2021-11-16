Given a list of non-negative numbers and a target integer k, write a function to check if the array has a continuous subarray of size at least 2 that sums up to the multiple of k, that is, sums up to n*k where n is also an integer.

Example 1:

Input: [23, 2, 4, 6, 7],  k=6
Output: True
Explanation: Because [2, 4] is a continuous subarray of size 2 and sums up to 6.

Example 2:

Input: [23, 2, 6, 4, 7],  k=6
Output: True
Explanation: Because [23, 2, 6, 4, 7] is an continuous subarray of size 5 and sums up to 42.
 

Note:

The length of the array won't exceed 10,000.
You may assume the sum of all the numbers is in the range of a signed 32-bit integer.



class Solution:
    def checkSubarraySum(self, nums: List[int], k: int) -> bool:
        
        # 1. Calculate the remainder and note the index into a dictionary =>  {remainder : index}
        # 2. If meet same remainder, check if the distince between indexes is > 1 then return true
        # 3. If k == 0: just return True
        # 4. Initialize the remainder_index dictionary with raminder = 0 for any sum after sum % k == 0
        
        remainder_index = {0 : -1}
        _sum = 0
        
        for idx, num in enumerate(nums):
            _sum += num
            # 0 is always a multiple of k
            if k == 0:
                return True
            else:
                remainder = _sum % k
                if remainder not in remainder_index:
                    remainder_index[remainder] = idx
                else:
                    if idx - remainder_index[remainder] > 1:
                        return True
        return False
        
        
