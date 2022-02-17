'''
Example:
Input: servers = [3,3,2], tasks = [1,2,3,2,1,2]
Output: [2,2,0,2,1,2]
Explanation: Events in chronological order go as follows:
- At second 0, task 0 is added and processed using server 2 until second 1.
- At second 1, server 2 becomes free. Task 1 is added and processed using server 2 until second 3.
- At second 2, task 2 is added and processed using server 0 until second 5.
- At second 3, server 2 becomes free. Task 3 is added and processed using server 2 until second 5.
- At second 4, task 4 is added and processed using server 1 until second 5.
- At second 5, all servers become free. Task 5 is added and processed using server 2 until second 7.
'''

class Solution:
    def assignTasks(self, servers: List[int], tasks: List[int]) -> List[int]:
        # Return server_id in the result
        ans = []
        # servers that are available
        available_servers = []
        # server handling tasks
        busy = []
        # server heap free: (weight, server_id)
        for server_id, weight in enumerate(servers):
            heapq.heappush(available_servers, (weight, server_id))
        # loop through tasks
        for sec, time_need in enumerate(tasks):
            # if next task start time == previous task ends time, release the server back to available servers list
            while busy and busy[0][0] == sec:
                _, weight, server_id = heapq.heappop(busy)
                heapq.heappush(available_servers, (weight, server_id))
            # If it has available servers
            if available_servers:
                weight, server_id = heapq.heappop(available_servers)
            # If there are no available servers, from the busy, pop the one which finish first
            else:
                sec, weight, server_id = heapq.heappop(busy)
            ans.append(server_id)
            heapq.heappush(busy, (sec + time_need, weight, server_id))
        return ans
