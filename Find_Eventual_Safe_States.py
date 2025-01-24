class Solution:
    def eventualSafeNodes(self, graph: List[List[int]]) -> List[int]:
        n = len(graph)
        safe = dict()

        def dfs(i):
            if i in safe:
                return safe[i]

            safe[i] = False

            for el in graph[i]:
                if not dfs(el):
                    return False
            
            safe[i] = True

            return True

        ans = []

        for i in range(n):
            if dfs(i):
                ans.append(i)
        
        return ans
