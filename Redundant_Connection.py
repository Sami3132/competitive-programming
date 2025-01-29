class Solution:
    def dfs(self, src, target, visited, adjList):
        visited[src] = True

        if src == target:
            return True

        isFound = False

        for adj in adjList[src]:
            if not visited[adj]:
                isFound = isFound or self.dfs(
                    adj, target, visited, adjList
                )

        return isFound

    def findRedundantConnection(self, edges):
        N = len(edges)

        adjList = [[] for _ in range(N)]

        for edge in edges:
            visited = [False] * N

            if self.dfs(edge[0] - 1, edge[1] - 1, visited, adjList):
                return edge

            adjList[edge[0] - 1].append(edge[1] - 1)
            adjList[edge[1] - 1].append(edge[0] - 1)

        return []
