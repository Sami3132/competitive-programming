class Solution:
    def punishmentNumber(self, n: int) -> int:
        total = 0

        def backtrack(i, curr, target, string):
            if i == len(string) and curr == target:
                return True
            
            for j in range(i, len(string)):
                if backtrack(j + 1, curr + int(string[i:j + 1]), target, string):
                    return True
            
            return False

        for i in range(1, n + 1):
            num = i * i
            if backtrack(0, 0, i, str(num)):
                total += num
        
        return total
