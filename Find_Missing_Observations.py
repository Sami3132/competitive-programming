class Solution:
    def missingRolls(self, rolls: List[int], mean: int, n: int) -> List[int]:
        m = len(rolls)
        nTotal = ((m + n) * mean) - sum(rolls)

        if nTotal > (n * 6) or nTotal < n:
            return []
        
        ans = []

        i = 1

        while nTotal:
            dice = min(nTotal - n + 1, 6)
            ans.append(dice)
            n -= 1
            nTotal -= dice
        
        return ans
