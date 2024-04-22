class Solution:
    def isValid(self, s: str) -> bool:
        myDict = {
            ')' : '(',
            '}' : '{',
            ']' : '[',
        }

        stack = []

        for bracket in s:
            if bracket not in myDict:
                stack.append(bracket)
            elif len(stack) != 0 and stack[-1] == myDict[bracket]:
                stack.pop()
            else:
                return False
        
        return not len(stack)
