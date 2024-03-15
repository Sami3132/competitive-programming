class Solution:
    def intervalIntersection(self, firstList: List[List[int]], secondList: List[List[int]]) -> List[List[int]]:
        ans = []
        l1, l2 = 0, 0

        while l1 != len(firstList) and l2 != len(secondList):
            f, s = firstList[l1], secondList[l2]

            if f[1] < s[0]:
                l1 += 1
                continue
            if f[0] > s[1]:
                l2 += 1
                continue
            
            left, right = max(f[0], s[0]), min(f[1], s[1])
            ans.append([left, right])

            if f[1] < s[1]:
                l1 += 1
            else:
                l2 += 1
        
        return ans
