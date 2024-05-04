class Solution:
    def decodeString(self, s: str) -> str:
        stack = []
        ans = ''
        multiple = 0

        for char in s:
            if char == '[':
                stack.append(ans)
                stack.append(multiple)
                multiple = 0
                ans = ''
            elif char == ']':
                first = stack.pop()
                second = stack.pop()
                ans = second + first * ans
            elif char.isdigit():
                multiple = multiple * 10 + int(char)
            else:
                ans += char
        
        return ans
