class Solution:
    def myAtoi(self, s: str) -> int:
        foundNum = False
        output = ""
        count = 0
        neg = False

        while count != len(s) and s[count] == " ":
            count += 1
        
        if count == len(s):
            return 0
        if s[count] == "-" or s[count] == "+":
            if s[count] == "-":
                neg = True
            count += 1
        
        while count != len(s) and s[count].isdigit():
            if s[count].isdigit():
                output += s[count]
            
            count += 1

        if len(output) == 0: return 0
        numb = int(output) if not neg else -int(output)
        
        if numb < -2 ** 31:
            return -2 ** 31
        elif numb > (2 ** 31 - 1):
            return (2 ** 31 - 1)
        else:
            return numb
