class Solution:
    def dfs_algo(self,node,adj,visited,result):
        visited[node] = 1
        result.append(node)
        
        for n in adj[node]:
            if visited[n] ==0:
                self.dfs_algo(n,adj,visited,result)
    def dfs(self, adj):
        n=len(adj)
        result = []
        visited = [0]*n
        self.dfs_algo(0,adj,visited,result)
        
        return result
        