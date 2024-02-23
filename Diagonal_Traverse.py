class Solution:
    def findDiagonalOrder(self, mat: List[List[int]]) -> List[int]:
        myDict = dict()
        output = []

        for i in range(len(mat)):
            for j in range(len(mat[0])):
                if (i + j) in myDict:
                    myDict[i + j].append(mat[i][j])
                else:
                    myDict[i + j] = [mat[i][j]]
        
        for key, value in myDict.items():
            if key % 2 == 0:
                value.reverse()
                output.extend(value)
            else:
                output.extend(value)
        return output
