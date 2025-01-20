class Solution:
    def firstCompleteIndex(self, arr: List[int], mat: List[List[int]]) -> int:
        n, m = len(mat), len(mat[0])
        row, col = defaultdict(int), defaultdict(int)

        myDict = dict()

        for i in range(n):
            for j in range(m):
                myDict[mat[i][j]] = (i, j)
        
        for i in range(len(arr)):
            hor, ver = myDict[arr[i]]

            row[hor] += 1
            col[ver] += 1

            if row[hor] == m or col[ver] == n:
                return i
