# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def sortList(self, head: Optional[ListNode]) -> Optional[ListNode]:
        def mergeSort(head):
            if not head or not head.next:
                return head
            
            left = head
            
            slow, fast = head, head.next

            while fast and fast.next:
                slow = slow.next
                fast = fast.next.next
            
            right = slow.next
            slow.next = None

            l = mergeSort(left)
            r = mergeSort(right)

            return merge(l, r)
        
        def merge(l, r):
            newList = ListNode()
            ptr = newList

            while l and r:
                if l.val < r.val:
                    ptr.next = l
                    l = l.next
                else:
                    ptr.next = r
                    r = r.next
                
                ptr = ptr.next
            
            if l:
                ptr.next = l

            if r:
                ptr.next = r
            
            return newList.next

        return mergeSort(head)
