Given an integer array nums, find the sum of the elements between indices i and j (i ≤ j), inclusive.

The update(i, val) function modifies nums by updating the element at index i to val.

Example:

Given nums = [1, 3, 5]

sumRange(0, 2) -> 9
update(1, 2)
sumRange(0, 2) -> 8
Note:

The array is only modifiable by the update function.
You may assume the number of calls to update and sumRange function is distributed evenly.

class NumArray:

    def __init__(self, nums: List[int]):
        self.sum_array = [0] * (len(nums)+1)
        self.nums = nums
        self.n = len(nums)
        for i in range(len(nums)):
            self.add(i+1, nums[i])
            
    def add(self,x,val):
        while x <= self.n:
            self.sum_array[x] += val
            x += self.lowbit(x)
            
    def lowbit(self,x):
        return x & -x
    
    def sum(self,x):
        res = 0
        while x >0:
            res += self.sum_array[x]
            x -= self.lowbit(x)
        return res

    def update(self, i: int, val: int) -> None:
        self.add(i + 1, val - self.nums[i])
        self.nums[i] = val

    def sumRange(self, i: int, j: int) -> int:
        if not self.nums: return  0
        return self.sum(j+1) - self.sum(i)


# Your NumArray object will be instantiated and called as such:
# obj = NumArray(nums)
# obj.update(i,val)
# param_2 = obj.sumRange(i,j)

