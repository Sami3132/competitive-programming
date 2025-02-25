class Solution:
    def numOfSubarrays(self, arr: List[int]) -> int:
            odd = even = total = ans = 0
            MOD = 10 ** 9 + 7

            for el in arr:
                total += el

                if total % 2:
                    ans = (ans + 1 + even) % MOD
                    odd += 1
                else:
                    ans = (ans + odd) % MOD
                    even += 1
            
            return ans
