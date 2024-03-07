class Solution:
    def judgeSquareSum(self, c: int) -> bool:
        if c == 0:
            return True
        squareRoot = math.sqrt(c)

        if math.floor(squareRoot) == squareRoot:
            return True
        
        num = math.floor(squareRoot)

        start = 0
        end = num

        while start <= end:
            if pow(start, 2) + pow(end, 2) == c:
                return True
            elif pow(start, 2) + pow(end, 2) < c:
                start += 1
            else:
                end -= 1

        return False
