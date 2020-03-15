from collections import defaultdict

def fun(A,k):
    mp=defaultdict(list)
    
    for i,v in enumerate(A):
        mp[abs(v)%k].append(i)
    
    print(mp)
    res = [v for k, v in mp.items() if len(v) > 1]
    print(res)
    res.sort(key=lambda x:len(x))
    return res[-1]


A=[-3,-2,1,0,8,7,1]
k=3
print(fun(A,k))

