class Solution:
    def findMinDifference(self, timePoints: List[str]) -> int:
        minutes = []

        for time in timePoints:
            h, m = int(time[:2]), int(time[3:])
            minutes.append(h * 60 + m)
        
        minutes.sort()
        
        ans = float("inf")

        for i in range(1, len(minutes)):
            ans = min(ans, minutes[i] - minutes[i - 1])

        ans = min(ans, 1440 - minutes[-1] + minutes[0])

        return ans
