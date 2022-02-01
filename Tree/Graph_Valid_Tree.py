class Solution:
    def validTree(self, n: int, edges: List[List[int]]) -> bool:
        '''
        valid tree basic condition:
        1. Graph contains no cycles.
        2. For every pair of nodes in Graph, there's a path between them
        '''
        
        # Doesn't meet condition 1
        if len(edges) != n - 1:
            return False
        
        if len(edges) == 0:
            return True
        # Create a neighbor list
        neighbor_lst = [ [] for _ in range(n)]
        for n1, n2 in edges:
            neighbor_lst[n1].append(n2)
            neighbor_lst[n2].append(n1)
        
        # Define a seen set to help bfs when determine if the neighbor has been seen before
        seen = set()
        # start with the first node which is 0
        # mainly for checking if we visited all nodes in the graph
        queue = collections.deque([0])
        while queue:
            node = queue.popleft()
            for neighbor in neighbor_lst[node]:
                if neighbor in seen:
                    continue
                seen.add(neighbor)
                queue.append(neighbor)
        return len(seen) == n
