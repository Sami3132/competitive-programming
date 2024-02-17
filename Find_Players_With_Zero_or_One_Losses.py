class Solution:
    def findWinners(self, matches: List[List[int]]) -> List[List[int]]:
        noLose = []
        oneLose = []
        myDict = dict()

        for winner, loser in matches:
            if loser in myDict:
                myDict[loser].append(winner)
            else:
                myDict[loser] = [winner]
            
            if winner not in myDict:
                myDict[winner] = []
        
        for el in myDict:
            if len(myDict[el]) == 0:
                noLose.append(el)
            elif len(myDict[el]) == 1:
                oneLose.append(el)
        noLose.sort()
        oneLose.sort()
        return [noLose, oneLose]
