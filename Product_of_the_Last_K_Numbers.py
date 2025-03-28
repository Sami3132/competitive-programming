class ProductOfNumbers:
    def __init__(self):
        self.stack = [1]
        self.size = 0

    def add(self, num: int):
        if num == 0:
            self.stack = [1]
            self.size = 0
        else:
            self.stack.append(self.stack[self.size] * num)
            self.size += 1

    def getProduct(self, k: int) -> int:
        if k > self.size:
            return 0
        return (
            self.stack[self.size] // self.stack[self.size - k]
        )



# Your ProductOfNumbers object will be instantiated and called as such:
# obj = ProductOfNumbers()
# obj.add(num)
# param_2 = obj.getProduct(k)
