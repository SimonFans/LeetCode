Example 1

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (4, 4)

Output: true
Explanation: One possible way is : left -> down -> left -> down -> right -> down -> right.


Example 2

Input 1: a maze represented by a 2D array

0 0 1 0 0
0 0 0 0 0
0 0 0 1 0
1 1 0 1 1
0 0 0 0 0

Input 2: start coordinate (rowStart, colStart) = (0, 4)
Input 3: destination coordinate (rowDest, colDest) = (3, 2)

Output: false
Explanation: There is no way for the ball to stop at the destination.



class Solution():
    # assume start and dest are tuple type
    def hasPath(self,maze,start,dest):

        def isvalid(x,y,maze):
            if x>=0 and x<len(maze) and y>=0 and y<len(maze[0]) and maze[x][y]==0:
                return True
            else:
                return False

        if len(maze)==0 or len(maze[0])==0 or len(start)==0 or len(dest)==0:
            return 0
        row,col=len(maze),len(maze[0])
        visited=set()
        directions = [(0, 1), (0, -1), (1, 0), (-1, 0)]
        queue=[]
        queue.append(start)
        visited.add(start)

        while queue:
            position=queue.pop(0)
            cur_x,cur_y=position[0],position[1]
            for i in range(len(directions)):
                next_x=cur_x
                next_y=cur_y

                while isvalid(next_x+directions[i][0],next_y+directions[i][1],maze):
                    next_x+=directions[i][0]
                    next_y=directions[i][1]
                if next_x==dest[0] and next_y==dest[1]:
                    return True
                if (next_x,next_y) not in visited:
                    visited.add((next_x,next_y))
                    queue.append((next_x,next_y))
        return False
