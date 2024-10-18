class Solution:
    def canArrange(self, arr: List[int], k: int) -> bool:
        n = len(arr)

        myDict = defaultdict(int)
        count = 0

        for num in arr:
            if myDict[num % k]:
                count += 1
                myDict[num % k] -= 1
            else:
                myDict[-num % k] += 1
        
        return True if count == n // 2 else False
