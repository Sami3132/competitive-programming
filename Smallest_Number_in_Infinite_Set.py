class SmallestInfiniteSet:

    def __init__(self):
        self.mySet = set()
        self.minVal = 1

    def popSmallest(self) -> int:
        if self.mySet:
            minimum = min(self.mySet)
            self.mySet.remove(minimum)
            return minimum
        else:
            self.minVal += 1
            return self.minVal - 1

    def addBack(self, num: int) -> None:
        if self.minVal > num:
            self.mySet.add(num)


# Your SmallestInfiniteSet object will be instantiated and called as such:
# obj = SmallestInfiniteSet()
# param_1 = obj.popSmallest()
# obj.addBack(num)
