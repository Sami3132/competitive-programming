class Solution:
    def findComplement(self, num: int) -> int:
        count = num.bit_length()

        mask = (1 << count) - 1
        
        return num ^ mask
