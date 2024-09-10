# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertGreatestCommonDivisors(self, head: Optional[ListNode]) -> Optional[ListNode]:
        curr = head

        while curr.next:
            numNode = ListNode(self.gcf(curr.val, curr.next.val))
            numNode.next = curr.next
            curr.next = numNode
            curr = numNode.next
        
        return head
        
    def gcf(self, num1, num2):
        maxNum, minNum = max(num1, num2), min(num1, num2)

        while minNum:
            minNum, maxNum = maxNum % minNum, minNum
        
        return maxNum
