# Google OA Compare strings

# A中最小字母在A中每个字符串出现的次数，如果比B中每个字符串最小字母数少，则算一个

# 1<=length of any string contained by A or B <=10


def solution(A,B):
    
    listA=A.split(' ')
    listB=B.split(' ')
    
    frequency=[0]*11
    for word in listA:
        min_freq=word.count(min(word))
        frequency[min_freq]+=1
    
    return_lst=[]
    for word in listB:
        min_freq=word.count(min(word))
        return_lst.append(sum(frequency[:min_freq]))
    
    return return_lst
    

"""
[0,2,1]
[3,2]
"""
A="abcd aabc bd"
B="aaa aa"

print(solution(A,B))
