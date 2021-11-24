'''
Given a positive integer n, generate an n x n matrix filled with elements from 1 to n2 in spiral order.
'''

# Case: Given n=3
# Output:
# 1 2 3
# 8 9 4
# 7 6 5

class Solution:
    def generateMatrix(self, n: int) -> List[List[int]]:
        res = [[0] * n for i in range(n)]
        cnt = 1
        # From out to inner layer
        # # of layers depend on the number (n+1)//2
        
        for layer in range((n+1)//2): 
            # top left to the top right:
            for ptr in range(layer, n-layer):
                res[layer][ptr] = cnt
                print('tl->tr:', cnt)
                cnt += 1
                
            # top right to the bottom right:
            for ptr in range(layer+1, n - layer):
                res[ptr][n-layer-1] = cnt
                print('tr-> br:', cnt)
                cnt += 1
                
            # bottom right to bottom left:
            for ptr in range(n-layer-2, layer-1, -1):
                res[n-layer-1][ptr] = cnt
                print('br-> bl:', cnt)
                cnt += 1
                
            # bottom left to top left:
            for ptr in range(n-layer-2, layer, -1):
                res[ptr][layer] = cnt
                print('bl-> tl:', cnt)
                cnt += 1
        return res
