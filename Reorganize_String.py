class Solution:
    def reorganizeString(self, s: str) -> str:
        count = Counter(s)
        heap = [[-count[k], k] for k in count]
        heapq.heapify(heap)

        ans = ""
        prev = [0, ""]

        while heap:
            curr = heapq.heappop(heap)
            ans += curr[1]

            if prev[0] < 0:
                heapq.heappush(heap, prev)

            curr[0] += 1
            prev = curr
            
        if len(ans) != len(s):
            return ""
        else:
            return ans
