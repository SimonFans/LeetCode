Given n, how many structurally unique BST's (binary search trees) that store values 1 ... n?

Example:

Input: 3
Output: 5
Explanation:
Given n = 3, there are a total of 5 unique BST's:

   1         3     3      2      1
    \       /     /      / \      \
     3     2     1      1   3      2
    /     /       \                 \
   2     1         2                 3
   
   
   
# Test 卡特兰尼公式
# dp[n]=dp[0]*dp[n-1]+dp[1]*dp[n-2]+... 

class Solution:
    def numTrees(self, n: int) -> int:
        dp=[1,1,2]
        if n<3:
            return dp[n]
        dp+=[0 for i in range(n-2)]
        for i in range(3,n+1):
            for j in range(1,i+1):
                dp[i]+=dp[j-1]*dp[i-j]
        
        return dp[n]
