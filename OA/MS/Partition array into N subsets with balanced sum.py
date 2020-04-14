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
