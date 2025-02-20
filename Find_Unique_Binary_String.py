class Solution:
    def findDifferentBinaryString(self, nums: List[str]) -> str:
        n = len(nums)
        nums = set(nums)

        def backtrack(string):
            if len(string) == n:
                if string not in nums:
                    return string

                return ""
            
            addZero = backtrack(string + "0")

            if addZero:
                return addZero
            
            return backtrack(string + "1")

        return backtrack("")
