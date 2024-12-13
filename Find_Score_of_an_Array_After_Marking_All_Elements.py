class Solution:
    def findScore(self, nums: List[int]) -> int:
        mySet = set()
        heap = []
        ans = 0

        for i in range(len(nums)):
            heapq.heappush(heap, (nums[i], i))
        
        while len(mySet) != len(nums) and heap:
            num, ind = heapq.heappop(heap)

            if ind not in mySet:
                ans += num
                mySet.add(ind)

                if ind != 0:
                    mySet.add(ind - 1)
                    
                if ind != len(nums) - 1:
                    mySet.add(ind + 1)
        
        return ans
