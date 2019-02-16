There are a total of n courses you have to take, labeled from 0 to n-1.

Some courses may have prerequisites, for example to take course 0 you have to first take course 1, which is expressed as a pair: [0,1]

Given the total number of courses and a list of prerequisite pairs, is it possible for you to finish all courses?

Example 1:

Input: 2, [[1,0]] 
Output: true
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0. So it is possible.
Example 2:

Input: 2, [[1,0],[0,1]]
Output: false
Explanation: There are a total of 2 courses to take. 
             To take course 1 you should have finished course 0, and to take course 0 you should
             also have finished course 1. So it is impossible.
Note:

The input prerequisites is a graph represented by a list of edges, not adjacency matrices. Read more about how a graph is represented.
You may assume that there are no duplicate edges in the input prerequisites.


class Solution(object):
    def canFinish(self, numCourses, prerequisites):
        """
        :type numCourses: int
        :type prerequisites: List[List[int]]
        :rtype: bool
        """
        # initialize 0 for each course
        inDegree=[0 for i in range(numCourses+1)]

        # create a course & its pre-course mapping
        Map={}
        if len(prerequisites)==0 or prerequisites==None:
            return True
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

        #queue.popleft()

        # BFS starts
        while len(queue):
            course=queue.popleft()
            subcourses=Map.get(course,[])    # [4], [4,5]

            for k in range(len(subcourses)):
                if inDegree[subcourses[k]]!=0:
                    inDegree[subcourses[k]]-=1
                    if inDegree[subcourses[k]]==0:
                        queue.append(subcourses[k])
                
            
        for i in range(numCourses+1):

            if inDegree[i]!=0:
                return False
        else:
            return True
