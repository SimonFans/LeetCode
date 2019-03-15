import collections
class Solution:
    def GetLevel(self, test, target):

        def fun(key):
            if key not in dic:
                return
            for i in dic[key]:
                fun(i)
                res.append(i)

        dic = collections.defaultdict(list)
        res=[]

        for boss, employee in test:
            if boss not in dic:
                dic[boss]=[employee]
            else:
                dic[boss].append(employee)

        for key in dic:
            if key==target:
                fun(key)

        return res


test=[['A','C'],['A','B'],['B','D'],['C','E'],['C','F'],['F','I'],['F','G']]
print(Solution().GetLevel(test,'C'))
