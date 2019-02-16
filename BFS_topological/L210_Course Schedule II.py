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

# 与207题差别就在于增加了个List/Array去记录每次popLeft()后的结果

class Solution(object):
    def findOrder(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: List[int]
        """
        # initialize 0 for each course
        inDegree=[0 for i in range(numCourses+1)]

        # create a course & its pre-course mapping
        Map={}
        
        # loop to let all course that need pre-course +=1, others no need are 0
        # Map find relationship, exp: 1->4, 2->[4,5]...
        for i in range(len(prerequisites)):
            inDegree[prerequisites[i][0]]+=1
            if prerequisites[i][1] not in Map:
                Map[prerequisites[i][1]]=[prerequisites[i][0]]
            else:
                Map[prerequisites[i][1]].append(prerequisites[i][0])
        
        # find all courses not need pre-course, append to queue
        queue=collections.deque()
        for i in range(numCourses):
            if inDegree[i]==0:
                queue.append(i)    #queue: [0,1,2]


        list_courses=[]
        # BFS starts
        while len(queue):
            course=queue.popleft()
            list_courses.append(course)
            subcourses=Map.get(course,[])    # [4], [4,5]

            for k in range(len(subcourses)):
                if inDegree[subcourses[k]]!=0:
                    inDegree[subcourses[k]]-=1
                    if inDegree[subcourses[k]]==0:
                        queue.append(subcourses[k])
        print(list_courses)
        if len(list_courses)==numCourses:
            return list_courses
        else:
            return []
