Given an array A of positive lengths, return the largest perimeter of a triangle with non-zero area, formed from 3 of these lengths.

If it is impossible to form any triangle of non-zero area, return 0.

 

Example 1:

Input: [2,1,2]
Output: 5
Example 2:

Input: [1,2,1]
Output: 0
Example 3:

Input: [3,2,3,4]
Output: 10
Example 4:

Input: [3,6,2,3]
Output: 8
 

Note:

3 <= A.length <= 10000
1 <= A[i] <= 10^6

class Solution:
    def largestPerimeter(self, A: List[int]) -> int:
        # 保证两个最小的边大于最大的边
        temp=[]
        A.sort()
        N=len(A)
        for i in range(N-1,-1,-1):
            temp.append(A[i])
        print(temp)
        # below define how many times for loop
        for i in range(N-2):
            if temp[i+1]+temp[i+2]>temp[i]:
                return temp[i+1]+temp[i+2]+temp[i]
        return 0
        
        
