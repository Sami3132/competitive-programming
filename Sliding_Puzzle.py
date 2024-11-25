class Solution:
    def slidingPuzzle(self, board: List[List[int]]) -> int:
        def simplify(newArr):
            return "".join(map(str, newArr))

        ans = float("inf")
        arr = [num for row in board for num in row]
        target = "123450"

        moves = {
            0: [1, 3], 1: [0, 2, 4], 2: [1, 5],
            3: [0, 4], 4: [1, 3, 5], 5: [2, 4]
        }
        
        zeroInd = arr.index(0)
        
        queue = deque([(arr, 0, zeroInd)])
        mySet = set()

        while queue:
            currArr, step, ind = queue.popleft()
            newStr = simplify(currArr)

            if newStr == target:
                return step
            
            if newStr in mySet:
                continue

            mySet.add(newStr)
            
            for nextInd in moves[ind]:
                newArr = currArr.copy()
                newArr[ind], newArr[nextInd] = newArr[nextInd], newArr[ind]
                queue.append((newArr, step + 1, nextInd))
        
        return -1
