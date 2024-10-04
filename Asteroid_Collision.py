class Solution:
    def asteroidCollision(self, asteroids: List[int]) -> List[int]:
        stack = []

        for asteroid in asteroids:
            while stack and stack[-1] > 0 and asteroid < 0:
                if abs(asteroid) < abs(stack[-1]):
                    asteroid = 0
                elif abs(asteroid) == abs(stack[-1]):
                    stack.pop()
                    asteroid = 0
                else:
                    stack.pop()
            
            if asteroid:
                stack.append(asteroid)
        
        return stack
