"""
Given an unsorted integer array, find the first missing positive integer.

For example,
Given [1,2,0] return 3,
and [3,4,-1,1] return 2.

[0,1, 2, 3]
[3,4,-1,1]
[1,-1,3,4]

"""

class solution:
    def First_Missing_Positive(self, A):
        length = len(A)
        for i in range(length):
            while A[i] > 0 and A[i] < length and A[A[i]-1] != A[i]:
                temp=A[A[i]-1]
                A[A[i] - 1]=A[i]
                A[i]=temp
        for j in range(length):
            if A[j] != j+1:
                return j+1
        return length+1

A=[3,4,-1,1]
test=solution()
print(test.First_Missing_Positive(A))