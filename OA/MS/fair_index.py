class Solution():
    def solution(self,A,B):
        count = 0
        sum_A = sum(A)
        sum_B = sum(B)
        left_A = 0
        left_B = 0
        for i in range(len(A)-1):
            left_A += A[i]
            left_B += B[i]
            if left_A == sum_A - left_A == left_B == sum_B - left_B: 
                #print(A[i], left_A, B[i],left_B)
                count += 1
        #print(count)
        return count

s = Solution()

assert s.solution([4,-1,0,3],[-2,5,0,3]) == 2
assert s.solution([4,-1,0,3],[-2,6,0,4]) == 0
assert s.solution([3,2,6],[4,1,6]) == 0
assert s.solution([1,4,2,-2,5],[7,-2,-2,2,5]) == 2
assert s.solution([2,-2,-3,3],[0,0,4,-4]) == 1
