class Solution:
    def kSmallestPairs(self, nums1, nums2, k):
        ans = []
        heap = [[x + nums2[0], 0] for x in nums1]

        while k > 0 and heap:
            el = heapq.heappop(heap)

            ans.append([el[0] - nums2[el[1]], nums2[el[1]]])

            if el[1] + 1 < len(nums2):
                heapq.heappush(heap, [el[0] - nums2[el[1]] + nums2[el[1] + 1], el[1] + 1])

            k -= 1

        return ans
