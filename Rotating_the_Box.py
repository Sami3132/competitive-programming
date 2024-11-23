class Solution:
    def rotateTheBox(self, box: List[List[str]]) -> List[List[str]]:
        for i in range(len(box)):
            empty = len(box[i]) - 1

            for j in range(len(box[i]) - 1, -1, -1):
                if box[i][j] == "#":
                    box[i][empty], box[i][j] = box[i][j], box[i][empty]
                    empty -= 1
                elif box[i][j] == "*":
                    empty = j - 1
        
        newArr = []
        
        for i in range(len(box[0])):
            arr = []

            for j in range(len(box) - 1, -1, -1):
                arr.append(box[j][i])
            
            newArr.append(arr)
        
        return newArr
