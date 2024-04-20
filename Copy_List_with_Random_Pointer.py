"""
# Definition for a Node.
class Node:
    def __init__(self, x: int, next: 'Node' = None, random: 'Node' = None):
        self.val = int(x)
        self.next = next
        self.random = random
"""

class Solution:
    def copyRandomList(self, head: 'Optional[Node]') -> 'Optional[Node]':
        if not head:
            return None

        curr = head
        myDict = dict()

        while curr:
            myDict[curr] = Node(curr.val)
            curr = curr.next
        
        curr = head

        while curr:
            myDict[curr].next = myDict.get(curr.next)
            myDict[curr].random = myDict.get(curr.random)
            curr = curr.next

        return myDict[head]
