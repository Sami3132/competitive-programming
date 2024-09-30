class CustomStack:

    def __init__(self, maxSize):
        self.n = maxSize
        self.stack = []
        self.ind = []

    def push(self, x):
        if len(self.ind) < self.n:
            self.stack.append(x)
            self.ind.append(0)

    def pop(self):
        if not self.ind: return -1
        if len(self.ind) > 1:
            self.ind[-2] += self.ind[-1]
        return self.stack.pop() + self.ind.pop()

    def increment(self, k, val):
        if self.ind:
            self.ind[min(k, len(self.ind)) - 1] += val
        


# Your CustomStack object will be instantiated and called as such:
# obj = CustomStack(maxSize)
# obj.push(x)
# param_2 = obj.pop()
# obj.increment(k,val)
