class Solution:
    def findRestaurant(self, list1: List[str], list2: List[str]) -> List[str]:
        myDict = dict()
        output = []
        count = float('inf')

        for i, el in enumerate(list1):
            myDict[el] = i
        
        for i, el in enumerate(list2):
            if el in myDict:
                if myDict[el] + i < count:
                    output = [el]
                    count = myDict[el] + i
                elif myDict[el] + i == count:
                    output.append(el)
                    count = myDict[el] + i
        
        return output
