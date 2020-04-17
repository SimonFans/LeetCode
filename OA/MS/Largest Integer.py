Write a function that, given an array A of N integers, 
returns the lagest integer K > 0 such that both values K and -K exist in array A. 
If there is no such integer, the function should return 0.

Example 1:

Input: [3, 2, -2, 5, -3]
Output: 3

Example 2:

Input: [1, 2, 3, -4]
Output: 0


from collections import defaultdict

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
