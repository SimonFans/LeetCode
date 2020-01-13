You are standing at position 0 on an infinite number line. There is a goal at position target.

On each move, you can either go left or right. During the n-th move (starting from 1), you take n steps.

Return the minimum number of steps required to reach the destination.

Example 1:

Input: target = 3
Output: 2
Explanation:
On the first move we step from 0 to 1.
On the second step we step from 1 to 3.

Example 2:

Input: target = 2
Output: 3
Explanation:
On the first move we step from 0 to 1.
On the second move we step  from 1 to -1.
On the third move we step from -1 to 2.

class Solution:
    def reachNumber(self, target: int) -> int:
        # target can be both positive and negative, but since axis is symmetric, so we can do abs()
        
        target=abs(target)
        # k: 1,2,3....
        k=0
        sum=0
        
        while sum<target:
            k+=1
            sum+=k
        # when walking steps beyond the target
        d=sum-target
        # 相当于前面有一步走反向，但还是当前k步
        if d%2==0:
            return k
        # if k is even, then return k+1. if k is odd, then return k+2 
        return k+1+(k%2)
        
        
