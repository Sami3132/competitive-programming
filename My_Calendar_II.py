class MyCalendarTwo:
    def __init__(self):
        self.myDict = defaultdict(int)

    def book(self, start: int, end: int) -> bool:
        self.myDict[start] += 1
        self.myDict[end] -= 1
        
        active_bookings = 0
        
        for time in sorted(self.myDict.keys()):
            active_bookings += self.myDict[time]
            
            if active_bookings >= 3:
                self.myDict[start] -= 1
                self.myDict[end] += 1
                
                if self.myDict[start] == 0:
                    del self.myDict[start]
                if self.myDict[end] == 0:
                    del self.myDict[end]
                
                return False
            
            if time > end:
                break
        
        return True
