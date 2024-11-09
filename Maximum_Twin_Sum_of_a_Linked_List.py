# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def pairSum(self, head: Optional[ListNode]) -> int:
        slow, fast = head, head.next
        stack = []
        ans = 0

        while fast.next:
            stack.append(slow.val)
            slow = slow.next
            fast = fast.next.next
        
        stack.append(slow.val)
        slow = slow.next

        while slow:
            ans = max(ans, slow.val + stack.pop())
            slow = slow.next
        
        return ans
