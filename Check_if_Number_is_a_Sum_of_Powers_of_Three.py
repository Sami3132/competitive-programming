class Solution:
    def checkPowersOfThree(self, n: int) -> bool:
        newArr = []
        limit = 10 ** 7

        power = 0

        while True:
            num = 3 ** power

            if num < limit:
                newArr.append(num)
                power += 1
            else:
                break

        total = 0

        print(newArr)

        for i in range(len(newArr) - 1, -1, -1):
            if newArr[i] == n:
                return True
            elif newArr[i] < n and total + newArr[i] <= n:
                total += newArr[i]
                if total == n:
                    return True
        
        return False
