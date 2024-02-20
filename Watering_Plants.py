class Solution:
    def wateringPlants(self, plants: List[int], capacity: int) -> int:
        steps = 0
        fullCapacity = capacity

        for i, plant in enumerate(plants):
            if plant > capacity:
                steps += 2 * i + 1
                capacity = fullCapacity - plant
            else:
                steps += 1
                capacity -= plant
        
        return steps
