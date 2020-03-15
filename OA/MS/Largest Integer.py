from collections import defaultdict

mp=defaultdict(list)

def largestInt(A):
    mp=set()
    largest=0
    for num in A:
        if -1*num in mp:
            if num>0:
                temp=num
            else:
                temp=-1*num
            if temp>largest:
                largest=temp
        else:
            mp.add(num)
    return largest

print(largestInt([3, 2, -2, 5, -3]))
