class MyCircularDeque:

  def __init__(self, k: int):
    self.deque = [None] * k
    self.k = k
    self.first = 0
    self.last = 0
    self.size = 0

  def insertFront(self, value: int) -> bool:
    if self.isFull():
        return False
    self.first = (self.first - 1) % self.k
    self.deque[self.first] = value
    self.size += 1
    return True

  def insertLast(self, value: int) -> bool:
    if self.isFull():
        return False
    self.deque[self.last] = value
    self.last = (self.last + 1) % self.k
    self.size += 1
    return True

  def deleteFront(self) -> bool:
    if self.isEmpty():
        return False
    self.first = (self.first + 1) % self.k
    self.size -= 1
    return True

  def deleteLast(self) -> bool:
    if self.isEmpty():
        return False
    self.last = (self.last - 1) % self.k
    self.size -= 1
    return True

  def getFront(self) -> int:
    if self.isEmpty():
        return -1
    return self.deque[self.first]

  def getRear(self) -> int:
    if self.isEmpty():
        return -1
    return self.deque[(self.last - 1) % self.k]

  def isEmpty(self) -> bool:
    return self.size == 0

  def isFull(self) -> bool:
    return self.size == self.k


# Your MyCircularDeque object will be instantiated and called as such:
# obj = MyCircularDeque(k)
# param_1 = obj.insertFront(value)
# param_2 = obj.insertLast(value)
# param_3 = obj.deleteFront()
# param_4 = obj.deleteLast()
# param_5 = obj.getFront()
# param_6 = obj.getRear()
# param_7 = obj.isEmpty()
# param_8 = obj.isFull()
