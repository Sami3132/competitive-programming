# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def swapNodes(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
        dummy = ListNode()
        dummy.next = head
        fast = slow = dummy


        for _ in range(k):
            fast = fast.next
        
        fastVal = fast

        while fast.next:
            fast = fast.next
            slow = slow.next
        
        slowVal = slow.next

        fastVal.val, slowVal.val = slowVal.val, fastVal.val

        return dummy.next
