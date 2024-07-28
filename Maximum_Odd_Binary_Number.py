class Solution:
    def maximumOddBinaryNumber(self, s: str) -> str:
        sortedArr = sorted(s, reverse = True)

        for i in range(len(s) - 1, -1, -1):
            if sortedArr[i] == '1':
                sortedArr[i], sortedArr[-1] = sortedArr[-1], sortedArr[i]
                break

        return ''.join(sortedArr)
