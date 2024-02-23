class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        length = len(digits) - 1

        if digits[length] + 1 < 10:
            digits[length] += 1
            return digits

        elif digits[length] + 1 == 10:
            while length - 1 != -1:
                if digits[length - 1] != 9:
                    digits[length] = 0
                    digits[length - 1] += 1
                    return digits
                else:
                    digits[length] = 0
                    length -= 1
            digits = [1] + [0] * len(digits)

        return digits
