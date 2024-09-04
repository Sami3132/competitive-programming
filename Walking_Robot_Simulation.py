class Solution:
    def robotSim(self, commands: List[int], obstacles: List[List[int]]) -> int:
        x, y = 0, 0
        direction = [[0, 1], [1, 0], [0, -1], [-1, 0]]
        direct = 0
        obstacles = {tuple(obstacle) for obstacle in obstacles}
        ans = 0

        for el in commands:
            if el == -1:
                direct = (direct + 1) % 4
            elif el == -2:
                direct = (direct - 1) % 4
            else:
                dx, dy = direction[direct]
                for i in range(el):
                    if ((x + dx), (y + dy)) in obstacles:
                        break
                    
                    x, y = x + dx, y + dy
            
            ans = max(ans, x ** 2 + y ** 2)
        
        return ans
