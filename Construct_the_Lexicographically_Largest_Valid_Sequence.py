class Solution:
    def constructDistancedSequence(self, n: int) -> List[int]:
        ans = [0] * (n * 2 - 1)
        used = [False] * (n + 1)
        self.backtrack(0, ans, used, n)

        return ans

    def backtrack(self, currInd, ans, used, n):
        if currInd == len(ans):
            return True

        if ans[currInd] != 0:
            return self.backtrack(currInd + 1, ans, used, n)

        for num in range(n, 0, -1):
            if used[num]:
                continue

            used[num] = True
            ans[currInd] = num

            if num == 1:
                if self.backtrack(currInd + 1, ans, used, n):
                    return True
            elif (currInd + num < len(ans) and ans[currInd + num] == 0):
                ans[currInd + num] = num

                if self.backtrack(currInd + 1, ans, used, n):
                    return True

                ans[currInd + num] = 0

            ans[currInd] = 0
            used[num] = False

        return False
