class Solution:
    def shortestDistanceAfterQueries(self, n: int, queries: List[List[int]]) -> List[int]:
        adj = [[i + 1] for i in range(n)]

        def bfs():
            queue = deque()
            queue.append((0, 0))
            mySet = set()
            mySet.add((0, 0))

            while queue:
                curr, length = queue.popleft()

                if curr == n - 1:
                    return length
                
                for neighbor in adj[curr]:
                    if neighbor not in mySet:
                        queue.append((neighbor, length + 1))
                        mySet.add((neighbor))
        
        ans = []

        for u, v in queries:
            adj[u].append(v)
            ans.append(bfs())
        
        return ans
