class Solution:
    def longestDiverseString(self, a: int, b: int, c: int) -> str:
        heap = []
        ans = ''

        if a > 0:
            heap.append((-a, 'a'))
        if b > 0:
            heap.append((-b, 'b'))
        if c > 0:
            heap.append((-c, 'c'))

        heapify(heap)

        while heap:
            curCount, curLetter = heappop(heap)
            n = len(ans)

            if n >= 2 and ans[n - 1] == curLetter and ans[n - 2] == curLetter:
                if not heap:
                    break
                
                nextCount, nextLetter = heappop(heap)

                ans += nextLetter
                nextCount += 1

                if nextCount < 0:
                    heappush(heap, (nextCount, nextLetter))
                
                heappush(heap, (curCount, curLetter))
            else:
                ans += curLetter
                curCount += 1

                if curCount < 0:
                    heappush(heap, (curCount, curLetter))
        
        return ans
