The Earliest Moment When Everyone Become Friends
In a social group, there are N people, with unique integer ids from 0 to N-1.

We have a list of logs, where each logs[i] = [timestamp, id_A, id_B] contains a non-negative integer timestamp, and the ids of two different people.

Each log represents the time in which two different people became friends.  Friendship is symmetric: if A is friends with B, then B is friends with A.

Let's say that person A is acquainted with person B if A is friends with B, or A is a friend of someone acquainted with B.

Return the earliest time for which every person became acquainted with every other person. Return -1 if there is no such earliest time.

 

Example 1:

Input: logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]], N = 6
Output: 20190301
Explanation: 
The first event occurs at timestamp = 20190101 and after 0 and 1 become friends we have the following friendship groups [0,1], [2], [3], [4], [5].
The second event occurs at timestamp = 20190104 and after 3 and 4 become friends we have the following friendship groups [0,1], [2], [3,4], [5].
The third event occurs at timestamp = 20190107 and after 2 and 3 become friends we have the following friendship groups [0,1], [2,3,4], [5].
The fourth event occurs at timestamp = 20190211 and after 1 and 5 become friends we have the following friendship groups [0,1,5], [2,3,4].
The fifth event occurs at timestamp = 20190224 and as 2 and 4 are already friend anything happens.
The sixth event occurs at timestamp = 20190301 and after 0 and 3 become friends we have that all become friends.
 

Note:

2 <= N <= 100
1 <= logs.length <= 10^4
0 <= logs[i][0] <= 10^9
0 <= logs[i][1], logs[i][2] <= N - 1
It's guaranteed that all timestamps in logs[i][0] are different.
logs are not necessarily ordered by some criteria.
logs[i][1] != logs[i][2]

"""
find(x):寻找x的根结点，当调用find的时候，实际上会施加一个tree compression method,把所有一条路上的节点都指向parent
rank: 树的复杂程度，通常把rank小的贴到rank大的上面去
"""


class UnionFindSet(object):
    # 初始化，roots存储所有节点信息，当前全部是指向自己，rank全部为0，意义为树的混乱程度
    def __init__(self, n):
        self.roots = [i for i in range(n)] # [0 1 2 3 4 5]
        self.rank = [0 for i in range(n)]  # [0 0 0 0 0 0]
        
    # 找到最早的parent结点是谁
    def find(self, member):
        if member!=self.roots[member]:
            member=self.find(self.roots[member])
        return member
    
    # 合并，当parent节点不同时，rank小的向rank大的靠拢，大的移动不方便，如果parent节点相同，随机指派一个作为parent节点，被指派为parent的节点rank+=1
    
    def union(self, p, q):
        parentP = self.find(p)
        parentQ = self.find(q)
        if parentP != parentQ:
            if self.rank[parentP] > self.rank[parentQ]:
                self.roots[parentQ] = parentP
            elif self.rank[parentP] < self.rank[parentQ]:
                self.roots[parentP] = parentQ
            else:
                self.roots[parentQ] = parentP
                self.rank[parentP] += 1
            
    
    def check(self):
        # flag 为roots[0]所对应节点的parent节点
        flag = self.find(self.roots[0])
        # 对于每一个在roots中的节点，看看是否都最终都归为一个parent
        for node in self.roots:
            if self.find(node) != flag:
                return False
        return True

class Solution(object):
    def earliestAcq(self, logs, N):
        """
        :type logs: List[List[int]]
        :type N: int
        :rtype: int
        """
        logs.sort(key=lambda x:x[0])
        ufs = UnionFindSet(N)
        for time, x, y in logs:
            ufs.union(x, y)
            if ufs.check():
                return time
        return -1

    
logs = [[20190101,0,1],[20190104,3,4],[20190107,2,3],[20190211,1,5],[20190224,2,4],[20190301,0,3],[20190312,1,2],[20190322,4,5]]
print(Solution().earliestAcq(logs,6))

