class Solution:
    def leastInterval(self, tasks: List[str], n: int) -> int:
        counter = Counter(tasks)
        heap = [(-count, task) for task, count in counter.items()]
        heapq.heapify(heap)

        ans = 0
        while heap:
            temp = []

            for _ in range(n + 1):
                if heap:
                    temp.append((heappop(heap)))
                else:
                    break

            for count, task in temp:
                if count + 1 < 0:
                    heappush(heap, (count + 1, task))

            ans += len(temp) if not heap else n + 1
                
        return ans
