from collections import defaultdict

def max_network_rank(A,B,N):
    
    res=float('-Inf')
    mp=defaultdict(list)
    for i in range(len(A)):
        mp[A[i]].append(B[i])
        mp[B[i]].append(A[i])
    print(mp)
    
    for i in range(len(A)):
        res=max(res,len(mp[A[i]])+len(mp[B[i]])-1)
    
    return res

A=[1,2,3,3]
B=[2,3,1,4]
N=4
print(max_network_rank(A,B,N))
