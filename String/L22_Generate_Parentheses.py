Given n pairs of parentheses, write a function to generate all combinations of well-formed parentheses.

For example, given n = 3, a solution set is:

[
  "((()))",
  "(()())",
  "(())()",
  "()(())",
  "()()()"
]


class Solution(object):
    def generateParenthesis(self, n):
        """
        :type n: int
        :rtype: List[str]
        """
        if n==0:
            return []
        res=[]
        self.helper(n,n,'',res)
        return res
    
    def helper(self,l,r,item,res):
        #剩余右括号数目小于剩余左括号数目，()()) filter 这种情况在append数组前
        if r<l:
            return
        # 满足条件的插入
        if l==0 and r==0:
            res.append(item)
        if l>0:
            self.helper(l-1,r,item+'(',res)
        if r>0:
            self.helper(l,r-1,item+')',res)
