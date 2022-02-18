There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, return the ordering of courses you should take to finish all courses.

There may be multiple correct orders, you just need to return one of them. If it is impossible to finish all courses, return an empty array.

Example 1:

Input: 2, [[1,0]] 
Output: [0,1]
Explanation: There are a total of 2 courses to take. To take course 1 you should have finished   
             course 0. So the correct course order is [0,1] .
Example 2:

Input: 4, [[1,0],[2,0],[3,1],[3,2]]
Output: [0,1,2,3] or [0,2,1,3]
Explanation: There are a total of 4 courses to take. To take course 3 you should have finished both     
             courses 1 and 2. Both courses 1 and 2 should be taken after you finished course 0. 
             So one correct course order is [0,1,2,3]. Another correct ordering is [0,2,1,3] .
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.

from collections import deque
class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        '''
        [[1,0],[2,0],[3,1],[3,2]]
        
        # create 0 that 0 has no prerequisite, 1 has 0 as prerequisite, ... 3 has 1 & 2 two prerequisites
        pre_condition => {0: set(), 1: (0), 2:(0), 3:(1,2)}
        
        # 0 has two neighbors 1 & 2,...
        graph = {0:(1,2), 1:(3), 2:(3)}
        
        '''
        # prerequisite {}
        pre_courses = {i: set() for i in range(numCourses)}
        # graph
        graph = collections.defaultdict(set)
        
        for i, j in prerequisites:
            pre_courses[i].add(j)
            graph[j].add(i)
        
        # return 
        order = []
        # used for bfs, find out which courses don't need pre-requisites, add to queue
        queue = deque()
        for k, v in pre_courses.items():
            if len(v) == 0:
                queue.append(k)
        
        # bfs starts
        while queue:
            course = queue.popleft()
            order.append(course)
            if len(order) == numCourses:
                return order
            for neighbor in graph[course]:
                # remove pre-requisites from any courses that depends on it
                pre_courses[neighbor].remove(course)
                # if and only if current course has no pre-requisites, this course is allowed to add into queue
                if not pre_courses[neighbor]:
                    queue.append(neighbor)
        return []
