class Solution:
    def numRescueBoats(self, people: List[int], limit: int) -> int:
        people.sort()

        if people[0] == limit:
            return len(people)
            
        left = 0
        right = len(people) - 1
        counter = 0

        while left <= right:
            if people[left] + people[right] <= limit:
                left += 1
            
            counter += 1
            right -= 1
        
        return counter
