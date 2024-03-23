class Solution:
	def subarraySum(self, nums: List[int], k: int) -> int:

		ans = 0 
		total = 0
		d = {0 : 1}

		for num in nums:
			total = total + num
			if total - k in d:
				ans = ans + d[total - k]
			if total not in d:
				d[total] = 1
			else:
				d[total] = d[total] + 1

		return ans
