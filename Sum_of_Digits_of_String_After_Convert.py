class Solution:
    def getLucky(self, s: str, k: int) -> int:
        newStr = ""

        for el in s:
            newStr += str(ord(el) - ord('a') + 1)
        
        for _ in range(k):
            sum = 0

            for el in newStr:
                sum += int(el)
            
            newStr = str(sum)
        
        return int(newStr)
