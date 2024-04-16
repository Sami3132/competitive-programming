# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
        if not head or left == right:
            return head
        
        newNode = ListNode()
        newNode.next = head
        prev = newNode
        range = right - left

        while left - 1:
            prev = prev.next
            left -= 1
        
        curr = prev.next

        while range:
            next = curr.next
            curr.next = next.next
            next.next = prev.next
            prev.next = next
            range -= 1
        
        return newNode.next
