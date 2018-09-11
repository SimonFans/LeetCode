class solution():

    count=0
    seen=set()

    def findCircleNum(self,M):
        for person in range(len(M)):
            if person not in self.seen:
                self.count+=1
                self.dfs(person,M,self.seen)
        return self.count

    def dfs(self,node,M,seen):
        for person, is_friend in enumerate(M[node]):
            if is_friend and person not in self.seen:
                self.seen.add(person)
                self.dfs(person,M,seen)




M=[[1,1,0],[1,1,0],[0,0,1]]
print(M)
print(type(M))
test=solution()
print(test.findCircleNum(M))