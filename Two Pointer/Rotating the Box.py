'''
You are given an m x n matrix of characters box representing a side-view of a box. Each cell of the box is one of the following:

A stone '#'
A stationary obstacle '*'
Empty '.'
The box is rotated 90 degrees clockwise, causing some of the stones to fall due to gravity. Each stone falls down until it lands on an obstacle, another stone, or the bottom of the box. Gravity does not affect the obstacles' positions, and the inertia from the box's rotation does not affect the stones' horizontal positions.

It is guaranteed that each stone in box rests on an obstacle, another stone, or the bottom of the box.

Return an n x m matrix representing the box after the rotation described above.
'''


Input: box = [["#",".","#"]]
Output: [["."],
         ["#"],
         ["#"]]
  
  
Input: box = [["#",".","*","."],
              ["#","#","*","."]]
Output: [["#","."],
         ["#","#"],
         ["*","*"],
         [".","."]]
  

Input: box = [["#","#","*",".","*","."],
              ["#","#","#","*",".","."],
              ["#","#","#",".","#","."]]
Output: [[".","#","#"],
         [".","#","#"],
         ["#","#","*"],
         ["#","*","."],
         ["#",".","*"],
         ["#",".","."]]
  
  
class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        row, col = len(box), len(box[0])        
        # For loop scan from the end of each row (Use example 2 )
        
        for r in range(row-1, -1, -1):
            # assume the previous obstacle position is the most right
            obstacle_pos = col
            for c in range(col-1,-1,-1):
                # If current pos is an obstacle:
                if box[r][c] == '*':
                    obstacle_pos = c
                    continue
                # when current pos is a stone:
                if box[r][c] == '#':
                    box[r][obstacle_pos-1], box[r][c] = box[r][c], box[r][obstacle_pos-1]
                    obstacle_pos -= 1
        print(box)
        # Lastly, return in 90 degrees clockwise:
        # After 90 degrees clockwise, row <-> col switch
        ans = []
        for j in range(col):
            temp = []
            for i in range(row-1,-1,-1):
                temp.append(box[i][j])
            ans.append(temp)
        return ans
      
      
      

  
  
 
 

