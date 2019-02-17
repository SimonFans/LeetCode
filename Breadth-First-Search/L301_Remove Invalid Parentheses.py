Remove the minimum number of invalid parentheses in order to make the input string valid. Return all possible results.

Note: The input string may contain letters other than the parentheses ( and ).

Example 1:

Input: "()())()"
Output: ["()()()", "(())()"]

Example 2:

Input: "(a)())()"
Output: ["(a)()()", "(a())()"]

Example 3:

Input: ")("
Output: [""]


class Solution:
    def removeInvalidParentheses(self, s: 'str') -> 'List[str]':
            
        """
        BFS solve 
        :type s: str
        :rtype: List[str]
        """
        if not s: return ['']
        q, ans, vis = [s], [], set([s])
        found = False
        while q:
            cur = q.pop(0)
            if self.isValidParentheses(cur):
                found = True
                ans.append(cur)
            elif not found:
                for i in range(len(cur)):
                    if cur[i] == '(' or cur[i] == ')':
                        t = cur[:i] + cur[i + 1:]
                        if t not in vis:
                            q.append(t)
                            vis.add(t)
                
        return ans

    def isValidParentheses(self, s):
        cnt = 0
        for c in s:
            if c == '(':
                cnt += 1
            elif c == ')':
                if cnt == 0: return False
                cnt -= 1
        return cnt == 0
        
