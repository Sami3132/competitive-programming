# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        if k == 0 or not head:
            return head
        
        counter = 1
        tail = head

        while tail.next:
            counter += 1
            tail = tail.next
        
        k = k % counter

        if k == 0 or k == counter:
            return head
        
        curr = head

        for _ in range(counter - k - 1):
            curr = curr.next
        
        newHead = curr.next
        curr.next = None
        tail.next = head

        return newHead
