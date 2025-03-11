class Solution:
    def numberOfSubstrings(self, s: str) -> int:
        n = len(s)
        l = ans = 0
        myDict = defaultdict(int)

        for r in range(n):
            myDict[s[r]] += 1

            while len(myDict) == 3:
                ans += (len(s) - r)
                myDict[s[l]] -= 1

                if myDict[s[l]] == 0:
                    del myDict[s[l]]
                l += 1
        
        return ans
