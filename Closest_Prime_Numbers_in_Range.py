class Solution:
    def closestPrimes(self, left: int, right: int) -> List[int]:
        primeNumber = [True for i in range(right + 1)]
        p = 2

        while p * p <= right:
            if primeNumber[p]:
                for i in range(p * p, right + 1, p):
                    primeNumber[i] = False

            p += 1
        
        primeNumber[1] = False

        curr = [[-1, -1], float("inf")]
        ans = [[-1, -1], float("inf")]

        while left <= right:
            if primeNumber[left]:
                if curr[0][1] != -1:
                    val = left - curr[0][1]
                    curr[0] = [curr[0][1], left]
                    curr[1] = val

                    if val < ans[1]:
                        ans = [[curr[0][0], curr[0][1]], val]
                elif curr[0][0] != -1:
                    val = left - curr[0][0]
                    curr[0][1] = left
                    curr[1] = val

                    if val < ans[1]:
                        ans = [[curr[0][0], curr[0][1]], val]
                else:
                    curr[0][0] = left

            left += 1
        
        return [-1, -1] if ans[0][1] == -1 else ans[0]
