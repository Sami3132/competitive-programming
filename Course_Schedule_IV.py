class Solution:
    def checkIfPrerequisite(self, numCourses: int, prerequisites: List[List[int]], queries: List[List[int]]) -> List[bool]: 
        if prerequisites == []:
            return [False] * len(queries)

        def bfs(f, l):
            queue = deque()
            visited = set()

            if myDict[f]:
                queue.append(myDict[f])
                visited.add(f)
                
            while queue:
                arr = queue.popleft()

                for el in arr:
                    if el not in visited:
                        visited.add(el)

                        if el == l:
                            return True
                        
                        if myDict[el]:
                            queue.append(myDict[el])

            return False

        ans = [False] * len(queries)

        myDict = defaultdict(list)

        for f, l in prerequisites:
            myDict[f].append(l)
    
        for i in range(len(queries)):
            f, l = queries[i]

            if bfs(f, l):
                ans[i] = True
        
        return ans
