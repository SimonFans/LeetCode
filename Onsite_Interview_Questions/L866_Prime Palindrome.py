Find the smallest prime palindrome greater than or equal to N.

Recall that a number is prime if it's only divisors are 1 and itself, and it is greater than 1. 

For example, 2,3,5,7,11 and 13 are primes.

Recall that a number is a palindrome if it reads the same from left to right as it does from right to left. 

For example, 12321 is a palindrome.

 

Example 1:

Input: 6
Output: 7
Example 2:

Input: 8
Output: 11
Example 3:

Input: 13
Output: 101
    
    
class Solution:
    def primePalindrome(self, N: int) -> int:
        while not self.isPalindrome(N) or not self.isPrime(N):
        
            N+=1

            # 跳过偶数位数, 偶数位的回文数都能被 11 整除
            if N > 10**1 and N < 10**2 and N != 11:
                N = 10**2
            if N > 10**3 and N < 10**4:
                N = 10**4
            if N > 10**5 and N < 10**6:
                N = 10**6
            if N > 10**7 and N < 10**8:
                N = 10**8
        return N

    
    def isPrime(self,n):
        if n==1:
            return False
        if n==2:
            return True
        else:
            for x in range(2,int(n**0.5)+1):
                if n%x==0:
                    return False
        return True

    def isPalindrome(self,n):
        t=str(n)
        l,r=0,len(t)-1
        while l<=r:
            if t[l]==t[r]:
                l+=1
                r-=1
            else:
                return False
        return True

    
        
