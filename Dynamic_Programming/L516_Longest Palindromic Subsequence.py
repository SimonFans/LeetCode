Given a string s, find the longest palindromic subsequence's length in s. You may assume that the maximum length of s is 1000.

Example 1:
Input:
"bbbab"

Output:
4

One possible longest palindromic subsequence is "bbbb".

Example 2:
Input:
"cbbd"

Output:
2

One possible longest palindromic subsequence is "bb".

Solution:

class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n=len(s)
        # create two dimensional array
        dp=[[0 for x in range(n)] for y in range(n)] 
        
        # l is how many chars each time count
        for l in range(1,n+1):
            for i in range(n-l+1):
                j=i+l-1
                if i==j:
                    dp[i][j]=1
                    continue
                
                if s[i]==s[j]:
                    dp[i][j]=2+dp[i+1][j-1]
                else:
                    dp[i][j]=max(dp[i][j-1],dp[i+1][j])
        return dp[0][n-1]



