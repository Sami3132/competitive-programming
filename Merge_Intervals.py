class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        intervals.sort()
        
        newArr = [intervals[0]]

        for i in range(1, len(intervals)):
            if intervals[i][0] > newArr[-1][1]:
                newArr.append(intervals[i])
            elif intervals[i][1] > newArr[-1][1]:
                newArr[-1][1] = intervals[i][1]
        
        return newArr
