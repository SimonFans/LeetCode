import collections
'''
# Time:  O(|V| + |E|)
# Space: O(|V| + |E|)
'''

class solution():

    def validTree(self, n, edges):
        if len(edges)!=n-1:
            return False

        # init node's neighbors in dict
        neighbors=collections.defaultdict(list)
        for u,v in edges:
            neighbors[u].append(v)
            neighbors[v].append(u)
        print(neighbors)

        # BFS to check if the graph is valid tree
        visited={}
        q=collections.deque([0])
        print(q)
        while q:
            curr=q.popleft()
            visited[curr]=True
            for node in neighbors[curr]:
                if node not in visited:
                    visited[node]=True
                    q.append(node)
        return len(visited)==n


n=5
edges1=[[0,1],[0,2],[0,3],[1,4]]
edges2=[[0,1],[1,2],[2,3],[1,3],[1,4]]
test=solution()
print(test.validTree(n,edges1))
print(test.validTree(n,edges2))