class NumberContainers:

    def __init__(self):
        self.indexCollection = defaultdict(SortedSet)
        self.indexVal = dict()

    def change(self, index: int, number: int) -> None:
        if index in self.indexVal:
            self.indexCollection[self.indexVal[index]].discard(index)

        self.indexVal[index] = number
        self.indexCollection[number].add(index)

    def find(self, number: int) -> int:
        return self.indexCollection[number][0] if self.indexCollection[number] else -1
        


# Your NumberContainers object will be instantiated and called as such:
# obj = NumberContainers()
# obj.change(index,number)
# param_2 = obj.find(number)
