class FrequencyTracker:
    def __init__(self):
        self.map = {}
        self.frequency = [0] * (10**5 + 1)

    def add(self, number):
        freq = self.map.get(number, 0)
        if freq > 0 and self.frequency[freq] > 0:
            self.frequency[freq] -= 1

        self.map[number] = freq + 1
        self.frequency[self.map[number]] += 1

    def deleteOne(self, n):
        count = self.map.get(n, 0)
        
        if count > 0:
            self.frequency[count] -= 1
            if count == 1:
                del self.map[n]
            else:
                self.map[n] = count - 1
                self.frequency[self.map[n]] += 1

    def hasFrequency(self, number):
        return number < len(self.frequency) and self.frequency[number] > 0

# Your FrequencyTracker object will be instantiated and called as such:
# obj = FrequencyTracker()
# obj.add(number)
# obj.deleteOne(number)
# param_3 = obj.hasFrequency(frequency)
