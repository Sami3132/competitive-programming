class Solution:
    def numberOfAlternatingGroups(self, colors: List[int], k: int) -> int:
        length = len(colors)
        result = 0
        cnt = 1
        curr = colors[0]

        for i in range(1, length + k - 1):
            index = i % length

            if colors[index] == curr:
                cnt = 1
                curr = colors[index]
                continue

            cnt += 1

            if cnt >= k:
                result += 1

            curr = colors[index]

        return result
