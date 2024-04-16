# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def isPalindrome(self, head: Optional[ListNode]) -> bool:
        slow = head
        fast = head

        while fast and fast.next:
            fast = fast.next.next
            slow = slow.next
        
        prev = slow
        slow = slow.next
        prev.next = None

        while slow:
            next = slow.next
            slow.next = prev
            prev = slow
            slow = next
        
        fast = head
        slow = prev

        while slow and fast:
            if fast.val != slow.val:
                return False
            
            fast = fast.next
            slow = slow.next

        return True
