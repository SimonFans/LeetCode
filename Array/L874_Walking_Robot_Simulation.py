A robot on an infinite XY-plane starts at point (0, 0) facing north. The robot can receive a sequence of these three possible types of commands:

-2: Turn left 90 degrees.
-1: Turn right 90 degrees.
1 <= k <= 9: Move forward k units, one unit at a time.
Some of the grid squares are obstacles. The ith obstacle is at grid point obstacles[i] = (xi, yi). If the robot runs into an obstacle, then it will instead stay in its current location and move on to the next command.

Return the maximum Euclidean distance that the robot ever gets from the origin squared (i.e. if the distance is 5, return 25).

Note:

North means +Y direction.
East means +X direction.
South means -Y direction.
West means -X direction.


Input: commands = [4,-1,3], obstacles = []
Output: 25
Explanation: The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 3 units to (3, 4).
The furthest point the robot ever gets from the origin is (3, 4), which squared is 32 + 42 = 25 units away.

Input: commands = [4,-1,4,-2,4], obstacles = [[2,4]]
Output: 65
Explanation: The robot starts at (0, 0):
1. Move north 4 units to (0, 4).
2. Turn right.
3. Move east 1 unit and get blocked by the obstacle at (2, 4), robot is at (1, 4).
4. Turn left.
5. Move north 4 units to (1, 8).
The furthest point the robot ever gets from the origin is (1, 8), which squared is 12 + 82 = 65 units away.


Input: commands = [6,-1,-1,6], obstacles = []
Output: 36
Explanation: The robot starts at (0, 0):
1. Move north 6 units to (0, 6).
2. Turn right.
3. Turn right.
4. Move south 6 units to (0, 0).
The furthest point the robot ever gets from the origin is (0, 6), which squared is 62 = 36 units away.


class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        '''
        此题技巧在于如何确定右转和左转的坐标位置。方法：找规律(0,1),(1,0),(0,-1),(-1,0)
        '''
        # obstacles from [[]] to {(),()...}
        obstacles = {(x, y) for x, y in obstacles}
        
        # question says the robot starts at point (0,0) facing north
        dx, dy = 0, 1
        
        # start point is origin, can be changed to any start points
        x, y = 0, 0
        
        # Euclidean distance
        dist = 0
        
        for command in commands:
            # Trun right
            if command == -1:
                dx, dy = dy, -dx
            # Turn left
            elif command == -2:
                dx, dy = -dy, dx
            else:
                # if meet obstacles then break and see what's the next command
                for _ in range(command):
                    if (x + dx, y + dy) in obstacles:
                        break
                    # go 1 step and keep looping
                    x, y = x + dx, y + dy
                # calculate the maximum Euclidean distance so far
                dist = max(dist, x**2 + y**2)
                
        return dist
                
                
