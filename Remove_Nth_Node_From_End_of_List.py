# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
        curr = head
        nextt = head

        for _ in range(n):
            nextt = nextt.next
        
        if not nextt:
            return head.next
        
        while nextt.next:
            nextt = nextt.next
            curr = curr.next
        
        curr.next = curr.next.next

        return head
