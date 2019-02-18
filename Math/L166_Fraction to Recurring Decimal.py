Given two integers representing the numerator and denominator of a fraction, return the fraction in string format.

If the fractional part is repeating, enclose the repeating part in parentheses.

Example 1:

Input: numerator = 1, denominator = 2
Output: "0.5"
Example 2:

Input: numerator = 2, denominator = 1
Output: "2"
Example 3:

Input: numerator = 2, denominator = 3
Output: "0.(6)"


class Solution:
    def fractionToDecimal(self, numerator: 'int', denominator: 'int') -> 'str':

        if numerator==0: return "0"
        # note down the reminder index in the array
        Map=dict()
        # do xor for answer if positive or negative
        ans = "-" if (numerator > 0) ^ (denominator > 0) else ""
        # let numerator and denominator both to be positive
        numerator,denominator = abs(numerator),abs(denominator)
        # get q and reminder
        q, r = divmod(numerator, denominator)
        # if can be dividable, then return q
        if r==0:
            return ans+str(q)
        ans+=str(q)+'.'
        # note down the reminder index in the array
        Map[r]=len(ans)
        while r:
            # reminder *10 / denominator
            r=r*10
            div,r=divmod(r,denominator)
            ans+=str(div)
            # if get same reminder, pull out the index and save the answer, then break
            if r in Map:
                index=Map[r]
                ans=ans[:index]+'('+ans[index:]+')'
                break
            else:
                Map[r]=len(ans)
        return ans
        
        
        print(Solution().fractionToDecimal(2,3))
        
        
