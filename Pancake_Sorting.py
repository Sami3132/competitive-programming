class Solution:
    def pancakeSort(self, arr: List[int]) -> List[int]:
        ans = []

        for i in range(len(arr), 0, -1):
            ind = arr.index(i)
            if ind != i - 1:
                if ind != 0:
                    ans.append(ind + 1)
                    arr = arr[:ind + 1][::-1] + arr[ind + 1:]
                ans.append(i)
                arr = arr[:i][::-1] + arr[i:]
        return ans
