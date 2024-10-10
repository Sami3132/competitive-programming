class Solution:
    def minAddToMakeValid(self, s: str) -> int:
        stack = []

        for el in s:
            if stack and el == ")" and stack[-1] == "(":
                stack.pop()
            else:
                stack.append(el)
         
        return len(stack)
