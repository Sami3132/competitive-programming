class Solution:
    def checkIfExist(self, arr: List[int]) -> bool:
        mySet = set()

        for i in range(len(arr)):
            if arr[i] in mySet:
                return True
            else:
                mySet.add(arr[i] * 2)
                if arr[i] % 2 == 0:
                    mySet.add(arr[i] / 2)
        
        if arr[i] in mySet:
                return True
        else:
                return False
