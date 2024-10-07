class Solution:
    def minLength(self, s: str) -> int:
        if len(s) == 1:
            return 1

        stack = []

        for el in s:
            if stack and ((stack[-1] == "A" and el == "B") or (stack[-1] == "C" and el == "D")):
                stack.pop()
            else:
                stack.append(el)
        
        return len(stack)
