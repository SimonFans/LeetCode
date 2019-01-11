# Question from Amazon Onsite

class Solution():
    def isPrime(self,n):
        if n==2:
            return True
        else:
            for x in range(2,n):
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

    def find_Prime(self,number):
        if number==1:
            return 2
        num=3
        count=1
        while(True):
            if self.isPrime(num) and self.isPalindrome(num):
                count+=1
                res=num      # save current result and return when finish
            num+=2   # avoid even number
            if count==number:   # stop when reach to the demand
                break

        return res

test=Solution()
number=6
print(test.find_Prime(number))
