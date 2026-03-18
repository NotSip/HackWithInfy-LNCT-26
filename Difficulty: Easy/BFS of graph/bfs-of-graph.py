from collections import deque
class Solution:
    def bfs(self, adj):
        start = 0
        ans = []
        queue = deque()
        n = len(adj)
        visited = [0]*(n)
        queue.append(start)
        visited[start] = 1
        
        while queue:
            u = queue.popleft()
            ans.append(u)
            
            for v in adj[u]:
                if visited[v] == 0:
                    visited[v] = 1
                    queue.append(v)
        
        return ans