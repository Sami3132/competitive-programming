class Solution:
    def matchPlayersAndTrainers(self, players: List[int], trainers: List[int]) -> int:
        players.sort()
        trainers.sort()

        p = 0
        t = 0
        counter = 0

        while t != len(trainers) and p != len(players):
            if players[p] <= trainers[t]:
                counter += 1
                p += 1
            
            t += 1
        
        return counter
