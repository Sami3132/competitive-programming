class Solution:
    def countPrimes(self, n: int) -> int:
        primeNums = [False] * (n)
        ans = 0

        for i in range(2, n):
            if not primeNums[i]:
                ans += 1

                for j in range(i * i, n, i):
                    primeNums[j] = True
                            
        return ans
