
# find # of friends for each one
input: [[A,B], [B,C], [A,C], [B,D], [E]]
output: {A:2, B:3, C:2, D:1, E:0}




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
                        res[susItem]=res.get(susItem)+1
            else:
                res[item[0]]=0
        return res
        
        
 
