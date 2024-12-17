class Solution:
    def repeatLimitedString(self, s: str, repeatLimit: int) -> str:
        myDict = Counter(s)
        heap = [(-ord(key), val) for key, val in myDict.items()]
        heapq.heapify(heap)

        ans = []

        while heap:
            currEl, currCount = heapq.heappop(heap)
            currEl = chr(-currEl)
            amount = min(currCount, repeatLimit)
            ans.append(currEl * amount)

            if currCount - amount > 0 and heap:
                nextEl, nextCount = heapq.heappop(heap)
                nextEl = chr(-nextEl)
                ans.append(nextEl)

                if nextCount > 1:
                    heapq.heappush(heap, (-ord(nextEl), nextCount - 1))
            
                heapq.heappush(heap, (-ord(currEl), currCount - amount))
        
        return "".join(ans)
