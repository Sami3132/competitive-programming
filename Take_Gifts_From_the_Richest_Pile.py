class Solution:
    def pickGifts(self, gifts: List[int], k: int) -> int:
        for i in range(len(gifts)):
            gifts[i] = -gifts[i]

        heapify(gifts)

        while k > 0:
            num = -(heappop(gifts))
            heappush(gifts, -floor(sqrt(num)))
            k -= 1

        return -sum(gifts)
