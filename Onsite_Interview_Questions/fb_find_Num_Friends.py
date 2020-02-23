
# find # of friends for each one
input: [[A,B], [B,C], [A,C], [B,D], [E]]
output: {A:2, B:3, C:2, D:1, E:0}

-- Solution1

class solution(object):
    def getFriendNum(self,friend):
        res=dict()
        # in case A knows C, C knows A duplicated count
        relation1=defaultdict(list)
        
        if len(friend)==0:
            return 0
        for item in friend:
            if len(item)>1:
                relation1[item[0]].append(item[1])
        
        for item in friend:
            if len(item)>1:
                if item[0] not in relation1[item[1]]:
                    relation1[item[1]].append(item[0])
            else:
                 relation1[item[0]]=[]
                
        
        # print(relation1)
        for i in relation1:
            res.update({i: len(relation1.get(i))})
        
        #print(res)
        return res    
        
    
# friends=[['D'],['A','B'],['A','C'],['C','A']]
friends=[['D'],['A','B'],['A','C'],['C','A'], ['B','A']]
print(solution().getFriendNum(friends))

-- Solution2

class solution(object):
    def getFriendNum(self,friend):
        res=dict()
        if len(friend)==0:
            return 0
        for item in friend:
            if len(item)>1:
                for susItem in item:
                    if susItem not in res:
                        res[susItem]=1
                    else:
                        res[susItem]+=1
            else:
                res[item[0]]=0
        return res

friends=[['A','B'], ['B','C'], ['A','C'], ['B','D'], ['E']]
print(solution().getFriendNum(friends))
        
 
