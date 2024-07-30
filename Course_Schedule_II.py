class Solution:
    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
        graph = defaultdict(list)
        incoming = [0 for _ in range(numCourses)]
        for cur, pre in prerequisites:
            graph[pre].append(cur)
            incoming[cur] += 1
        
        queue = deque()
        ans = []

        for i in range(numCourses):
            if incoming[i] == 0:
                queue.append(i)
        
        while queue:
            curr = queue.popleft()
            ans.append(curr)

            for el in graph[curr]:
                incoming[el] -= 1
                if incoming[el] == 0:
                    queue.append(el)
        
        return [] if len(ans) != numCourses else ans
