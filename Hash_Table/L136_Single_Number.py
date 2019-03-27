Given a non-empty array of integers, every element appears twice except for one. Find that single one.

Note:

Your algorithm should have a linear runtime complexity. Could you implement it without using extra memory?

Example 1:

Input: [2,2,1]
Output: 1
Example 2:

Input: [4,1,2,1,2]
Output: 4


## dictionary.pop(i) 将当前的key i remove

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        hash_table = {}
        for i in nums:
            if i in hash_table:
                hash_table.pop(i)
            else:
                hash_table[i] = 1
        return hash_table.popitem()[0]
