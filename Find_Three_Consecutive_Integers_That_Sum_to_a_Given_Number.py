class Solution:
    def sumOfThree(self, num: int) -> List[int]:
        if num % 3 == 0:
            divide = (num // 3)
            return [divide - 1, divide, divide + 1]
        else:
            return []
