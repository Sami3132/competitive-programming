class Solution:
    def findTheWinner(self, n: int, k: int) -> int:
        if k == 1: return n

        players = [player for player in range(1, n + 1)]
        count = 0

        for i in range(n - 1):
            count = (count + k - 1) % (n - i)
            players.pop(count)

        return players[0]
