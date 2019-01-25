A string of '0's and '1's is monotone increasing if it consists of some number of '0's (possibly 0), followed by some number of '1's (also possibly 0.)

We are given a string S of '0's and '1's, and we may flip any '0' to a '1' or a '1' to a '0'.

Return the minimum number of flips to make S monotone increasing.

 

Example 1:

Input: "00110"
Output: 1
Explanation: We flip the last digit to get 00111.
Example 2:

Input: "010110"
Output: 2
Explanation: We flip to get 011111, or alternatively 000111.
Example 3:

Input: "00011000"
Output: 2
Explanation: We flip to get 00000000.


class Solution:
    def minFlipsMonoIncr(self, S):
        """
        :type S: str
        :rtype: int
        """
        zero=[0]*len(S)
        one=[0]*len(S)
        if S[0]=="0":
            one[0]=1
        else:
            zero[0]=1
            #当前之位是0，变0不用动，变1可以是0001 or 1111, 0->1 再加1
        for i in range(len(S)):
            if S[i]=="0":
                zero[i]=zero[i-1]
                one[i]=min(zero[i-1],one[i-1])+1
            else:
                zero[i]=zero[i-1]+1
                one[i]=min(zero[i-1],one[i-1])
        return min(zero[i],one[i])
        
        
