# Count submatrices with all ones 


def countSubmatrices(matrix):
    # Get #row of sample matrix
    n = len(matrix)
    # Get #columns of sample matrix
    m = len(matrix[0])
    # Create an answer matrix (n+1, m+1) with all 0s 
    ans_matrix = [[0]*(m+1) for _ in range(n+1)]
    # define a variable to return
    cnt = 0 
    
    for row in range(1, n+1):
        for col in range(1, m+1):
            '''if the given matrix element value == 1, then get the minium value via comparing its left, up and upper-left then plus 1,
            which means how many submatrix the current positon can have, the final result is to sum up all numbers in the answer matrix.
            '''
            if matrix[row-1][col-1]== 1:
                ans_matrix[row][col] = 1 + min(ans_matrix[row][col-1], ans_matrix[row-1][col], ans_matrix[row-1][col-1])
                cnt += ans_matrix[row][col]
    return cnt

# Sample data 
# Expect to return 15

matrix = [[0,1,1,1],[1,1,1,1],[0,1,1,1]]
print(matrix)
print(countSubmatrices(matrix))


# Refer to: https://www.youtube.com/watch?v=ojz8xZc8pog

