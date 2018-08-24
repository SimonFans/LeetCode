"""
Input: S = "ADOBECODEBANC", T = "ABC"

Output: "BANC

"""
import sys

def min_window_substring(S,T):
    count={}
    for i in range(len(S)):
        count[S[i]]=0
    for i in range(len(T)):
        count[T[i]]=count.get(T[i])+1

    start=0
    total=len(T)
    min=sys.maxsize
    j=0
    for i in range(len(S)):
        if count.get(S[i])>0:
            total-=1
        count[S[i]]=count.get(S[i])-1



        while total==0:
            if i-j+1< min:
                min=i-j+1
                start=j
                #print(start)


            count[S[j]]=count.get(S[j]) + 1
            if count.get(S[j])>0:

                total+=1
            j+=1

    return "" if min==sys.maxsize else S[start:start+min]


S = "ADOBECODEBANC"
T = "ABC"
print(min_window_substring(S,T))
