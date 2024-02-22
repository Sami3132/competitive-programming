class Solution:
    def minOperations(self, boxes: str) -> List[int]:
        myDict = {}
        output = []

        for i in range(len(boxes)):
            if boxes[i] == '1':
                if 1 in myDict:
                    myDict[1].append(i)
                else:
                    myDict[1] = [i]
        
        for i in range(len(boxes)):
            total = 0

            for j in myDict.get(1, []):
                total += abs(j - i)
            
        
            output.append(total)
        return output
