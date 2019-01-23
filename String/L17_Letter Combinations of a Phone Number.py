Given a string containing digits fr

om 2-9 inclusive, return all possible letter combinations that the number could represent.

A mapping of digit to letters (just like on the telephone buttons) is given below. Note that 1 does not map to any letters.



Example:

Input: "23"
Output: ["ad", "ae", "af", "bd", "be", "bf", "cd", "ce", "cf"].
Note:

Although the above answer is in lexicographical order, your answer could be in any order you want.


class Solution:
    def letterCombinations(self, digits):
        """
        :type digits: str
        :rtype: List[str]
        """
        
        def dfs(num,string,res):
            
            dict1 = {'2':['a','b','c'],
                    '3':['d','e','f'],
                    '4':['g','h','i'],
                    '5':['j','k','l'],
                    '6':['m','n','o'],
                    '7':['p','q','r','s'],
                    '8':['t','u','v'],
                    '9':['w','x','y','z']
                    }
            
            if num==length:
                res.append(string)
                return
            for i in dict1[digits[num]]:
                dfs(num+1,string+i,res)
        
        if not len(digits):
            return []
        res=[]
        length=len(digits)
        dfs(0,'',res)
        return res
