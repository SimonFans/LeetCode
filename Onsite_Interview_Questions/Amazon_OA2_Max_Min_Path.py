"""
8   4   7

6   5   9
"""
#

class solution():
    def Max_Min_Path(self,matrix):
        result=[0]*len(matrix[0])
        result[0]=matrix[0][0]
        for i in range(1,len(matrix[0])):
            result[i]=min(result[i-1],matrix[0][i])

        for i in range(1,len(matrix)):
            result[0]=min(result[0],matrix[i][0])
            for j in range(1,len(matrix[0])):
                if result[j-1]<matrix[i][j] and result[j]<matrix[i][j]:
                    result[j]=max(result[j-1],result[j])
                else:
                    result[j]=matrix[i][j]
        return result[len(matrix[0])-1]


matrix=[[8,4,7],[6,5,9]]
print(solution().Max_Min_Path(matrix))
