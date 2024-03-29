class Solution:
    def shiftingLetters(self, s: str, shifts: List[int]) -> str:
        s = list(s)
        shifts[len(shifts) - 1] %= 26

        for i in range(len(shifts) - 1, 0, -1):
            shifts[i - 1] += shifts[i]

        for i in range(len(shifts)):
            if shifts[i] >= 26:
                shifts[i] %= 26
            
            if ord(s[i]) + shifts[i] > ord('z'):
                s[i] = chr(ord(s[i]) + shifts[i] - 26)
            else:
                s[i] = chr((ord(s[i]) + shifts[i]))
        
        return "".join(s)
