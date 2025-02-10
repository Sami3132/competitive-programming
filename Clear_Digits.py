class Solution:
    def clearDigits(self, s: str) -> str:
        stack = []
        nums = ["1", "2", "3", "4", "5", "6", "7", "8", "9", "0"]

        for el in s:
            if el not in nums:
                stack.append(el)
            else:
                stack.pop()
        
        return "".join(stack)
