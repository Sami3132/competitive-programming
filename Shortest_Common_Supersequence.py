class Solution:
    def shortestCommonSupersequence(self, str1: str, str2: str) -> str:
        str1Len = len(str1)
        str2Len = len(str2)

        dp = [
            [0 for _ in range(str2Len + 1)] for _ in range(str1Len + 1)
        ]

        for row in range(str1Len + 1):
            dp[row][0] = row

        for col in range(str2Len + 1):
            dp[0][col] = col

        for row in range(1, str1Len + 1):
            for col in range(1, str2Len + 1):
                if str1[row - 1] == str2[col - 1]:
                    dp[row][col] = dp[row - 1][col - 1] + 1
                else:
                    dp[row][col] = min(dp[row - 1][col], dp[row][col - 1]) + 1

        newArr = []
        row, col = str1Len, str2Len

        while row > 0 and col > 0:
            if str1[row - 1] == str2[col - 1]:
                newArr.append(str1[row - 1])
                row -= 1
                col -= 1
            elif dp[row - 1][col] < dp[row][col - 1]:
                newArr.append(str1[row - 1])
                row -= 1
            else:
                newArr.append(str2[col - 1])
                col -= 1

        while row > 0:
            newArr.append(str1[row - 1])
            row -= 1
        while col > 0:
            newArr.append(str2[col - 1])
            col -= 1

        return "".join(newArr[::-1])
