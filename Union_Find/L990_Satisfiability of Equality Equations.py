'''
Given an array equations of strings that represent relationships between variables, each string equations[i] has length 4 and takes one of two different forms: "a==b" or "a!=b".  Here, a and b are lowercase letters (not necessarily different) that represent one-letter variable names.

Return true if and only if it is possible to assign integers to variable names so as to satisfy all the given equations.

Input: ["a==b","b!=a"]
Output: false
Explanation: If we assign say, a = 1 and b = 1, then the first equation is satisfied, but not the second.  There is no way to assign the variables to satisfy both equations.

Input: ["b==a","a==b"]
Output: true
Explanation: We could assign a = 1 and b = 1 to satisfy both equations.

Input: ["a==b","b==c","a==c"]
Output: true

Input: ["a==b","b!=c","c==a"]
Output: false

Input: ["c==c","b==d","x!=z"]
Output: true
'''


Solution:

class Solution:
    def equationsPossible(self, equations: List[str]) -> bool:
        # 建立26个子list分别存储对应的26个字符与那些字母下标相连
        graph = [[] for _ in range(26)]
        
        # 遍历整个list，相对于==进行处理，对等号两边字符分别求取对应下标值，将下标值添加到各自的graph子list中
        for eqn in equations:
            if eqn[1] == '=':
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')
                graph[x].append(y)
                graph[y].append(x)
                
        color = [None] * 26
        t = 0
        # start每个子list的下标
        for start in range(26):
            if color[start] is None:
                t += 1
                stack = [start]
                while stack:
                    node = stack.pop()
                    for nei in graph[node]:
                        if color[nei] is None:
                            color[nei] = t
                            stack.append(nei)
        # 最后对于!=的进行讨论
        for eqn in equations:
            if eqn[1] == '!':
                x = ord(eqn[0]) - ord('a')
                y = ord(eqn[3]) - ord('a')
                # example: a!=a => return false
                if x == y: return False 
                # color[x]为空：例如最后一个case，x不与任何node相连
                if color[x] is not None and color[x] == color[y]:
                    return False
        return True
      
      
      
