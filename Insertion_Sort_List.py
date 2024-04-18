# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def insertionSortList(self, head: ListNode) -> ListNode:
        if not head or not head.next:
            return head
        
        dummy = ListNode(-5000, head)
        sortedLargest = head
        curr = head.next

        while curr:
            if curr.val >= sortedLargest.val:
                sortedLargest = sortedLargest.next
            else:
                prev = dummy
                
                while prev.next.val <= curr.val:
                    prev = prev.next
                    
                sortedLargest.next = curr.next
                curr.next = prev.next
                prev.next = curr
                
            curr = sortedLargest.next
            
        return dummy.next
