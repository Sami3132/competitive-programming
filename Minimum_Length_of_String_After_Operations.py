class Solution:
    def minimumLength(self, s: str) -> int:
        count = 0

        myDict = Counter(s)

        for val in myDict.values():
            if val > 2:
                if val % 2:
                    count += val - 1
                else:
                    count += val - 2

        return len(s) - count
