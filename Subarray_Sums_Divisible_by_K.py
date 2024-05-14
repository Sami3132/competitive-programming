class Solution:
    def subarraysDivByK(self, nums: List[int], k: int) -> int:
        prefix_sum = 0
        sums = {0: 1}
        answer = 0
        for num in nums:
            prefix_sum += num
            key = prefix_sum % k

            if key in sums:
                answer += sums[key]
                sums[key] += 1
                continue

            sums[key] = 1
            
        return answer
