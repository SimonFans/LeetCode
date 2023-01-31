func canFinish(numCourses int, prerequisites [][]int) bool {
    /*
    Let's assume prerequisites = [[1,0],[2,1]] which means course 1 has a prerequisite course 0, and 
    course 2 has a prerequisite course 1. 
    */
    // each course takes up one position count
    indegree := make([]int, numCourses) // [0,0,0]
    // graph describes the dependency between target course and prerequisite course
    graph := make([][]int, numCourses) // [[],[],[]]
    for _, prerequisite := range prerequisites {
		source := prerequisite[1]                  // prerequisite
		target := prerequisite[0]               // target
		graph[source] = append(graph[source], target) 
         /*
        graph = [ [1],   [2],     []] 
        course1 has a prerequisite course 0 (graph[0])
        course2 has a prerequisite course 1 (graph[1])
        */
    indegree[target] += 1
        // [0,1,1] course 1 has one prerequisite, course 2 has one prerequisite
    }
    queue := make([]int, 0) // [] initilize a queue to store courses without prerequites
    // find out the courses without prerequisites via loop through the indegree slice 
    for course, degree := range indegree {
	if degree == 0 {
	    queue = append(queue, course) // add courses without prerequisites into a queue
	}
    }
    /*
    For those courses which don't have prerequisites 
    pop from the queue and get all its dependency courses
    minus 1 for each of them in the indegree slice
    determine if they don't have prerequistes via a if condition indegree[next] == 0
    If they really don't have any prerequisites, add it into the queue 
    */
    for len(queue) != 0 {
		course := queue[0]
		queue = queue[1:]
		for _, next := range graph[course] {
			indegree[next] -= 1
			if indegree[next] == 0 {
				queue = append(queue, next)
			}
		}
	}
    /*
    Finally, when the queue is empty, check if each value in indegree slice equals to zero (zero means
    this course can be finished since its prerequisites has been gone through)
    If it is, then return true. If it's not, return false. 
    */
    for _, val := range indegree {
		if val != 0 {
			return false
		}
	}
    return true
}
