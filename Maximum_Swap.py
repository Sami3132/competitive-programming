class Solution:
    def maximumSwap(self, num: int) -> int:
        num = list(str(num))

        maxVal = "0"
        maxInd = -1

        swapI = swapJ = -1

        for i in range(len(num) - 1, -1, -1):
            if num[i] > maxVal:
                maxVal = num[i]
                maxInd = i
            if num[i] < maxVal:
                swapI, swapJ = i, maxInd
        
        if swapI != -1:
            num[swapI], num[swapJ] = num[swapJ], num[swapI]
        
        return int("".join(num))
