class Solution:
    def queryResults(self, limit: int, queries: List[List[int]]) -> List[int]:
        arr = defaultdict(int)
        myDict = defaultdict(int)
        count = 0
        ans = [0] * len(queries)

        for i in range(len(queries)):
            x, y = queries[i]

            if x not in arr:
                arr[x] = y
                myDict[y] += 1

                if myDict[y] == 1:
                    count += 1
            elif x in arr:
                myDict[arr[x]] -= 1

                if myDict[arr[x]] == 0:
                    count -= 1
                
                myDict[y] += 1
                arr[x] = y

                if myDict[y] == 1:
                    count += 1

            ans[i] = count

        return ans
