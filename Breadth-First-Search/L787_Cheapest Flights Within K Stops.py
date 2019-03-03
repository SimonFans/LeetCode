There are n cities connected by m flights. Each fight starts from city u and arrives at v with a price w.

Now given all the cities and flights, together with starting city src and the destination dst, 
your task is to find the cheapest price from src to dst with up to k stops. If there is no such route, output -1.

Example 1:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 1
Output: 200
Explanation: 
The graph looks like this:


The cheapest price from city 0 to city 2 with at most 1 stop costs 200, as marked red in the picture.


Example 2:
Input: 
n = 3, edges = [[0,1,100],[1,2,100],[0,2,500]]
src = 0, dst = 2, k = 0
Output: 500

class Solution:
    def findCheapestPrice(self, n: int, flights: List[List[int]], src: int, dst: int, K: int) -> int:
        
        adj = collections.defaultdict(dict)
        for u, v, w in flights:

            adj[u][v] = w
        # defaultdict(<class 'dict'>, {0: {1: 100, 2: 500}, 1: {2: 100}})
        pq = [(0, src, -1)]
        
        while pq:
            cost, s, k = heapq.heappop(pq)
        
            if s == dst: return cost
            if k < K:
                for t in adj[s]:
                    heapq.heappush(pq, (cost + adj[s][t], t, k + 1))
        return -1
