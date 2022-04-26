Give you one sorted array, please put them into n buckets, we need to ensure we get n sub array with approximately equal weights.
Example;
input {1, 2, 3, 4, 5} n = 3
output [[[5],[1,4],[2,3]];


"""
      0  1  2  3  4  5  6
A =  [4, 3, 2, 3, 5, 2, 1]  k = 4 , target = 5
                []
i = 0      [4]                                                    
           [4,3] [4,2] [4,3] [4,5] [4,2] [4,1](meet)                 
i = 1      [3] 
           [3,2](meet)
i = 2      [2](unavailable)
i = 3      [3]
           [3,5] [3,2](meet)
i = 4      [5](meet)
i = 5      [2](unavailable)
i = 6      [1](unavailable)

           
    
"""
"""
      0  1  2  3  4  5  6
A =  [4, 3, 2, 3, 5, 2, 1]  k = 4 , target = 5

               
"""

class Solution():
    def solution(self,A,K):
        self.output = []
        target = sum(A) // K
        visited =set()
        self.backtracking([],0,A,target,visited)
        print(self.output)
        return len(self.output) == K
    def backtracking(self,subset,index,A,target,visited):
        if target == 0:
            self.output.append(list(subset))
        elif target < 0:
            return 
        print(subset,visited,self.output)
        for i in range(index,len(A)):
            if i not in visited:
                visited.add(i)
                self.backtracking(subset+[A[i]],i,A,target - A[i],visited)
                visited.remove(i)
        
            
s = Solution()

assert s.solution([4, 3, 2, 3, 5, 2, 1],4) == True
        
print("pass all test case")
        

        class Solution:
    def canPartitionKSubsets(self, arr: List[int], k: int) -> bool:
        def backtrack(count: int, curr_sum: int) -> bool:
        # We made k - 1 subsets with target sum and the last subset will also have target sum.
            if count == k - 1:
                return True
            # Current subset-sum exceeds target sum, no need to proceed further.
            if curr_sum > target_sum:
                return False
            # When current subset sum reaches target sum then one subset is made.
            # Increment count and reset current subset sum to 0.
            if curr_sum == target_sum:
                return backtrack(count + 1, 0)
            # Try not picked elements to make some combinations.
            for j in range(n):
                if not taken[j]:
            # Include this element in current subset.
                    taken[j] = True
            # If using current jth element in this subset leads to make all valid subsets.
                    if backtrack(count, curr_sum + arr[j]):
                        return True
            # Backtrack step.
                    taken[j] = False
            # We were not able to make a valid combination after picking
            # each element from the array, hence we can't make k subsets.
            return False
        total_array_sum = sum(arr)
        n = len(arr)
        # If the total sum is not divisible by k, we can't make subsets.
        if total_array_sum % k != 0:
            return False
        target_sum = total_array_sum // k
        taken = [False] * n
        return backtrack(0, 0)
        
        
