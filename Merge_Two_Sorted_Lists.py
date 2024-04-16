# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def mergeTwoLists(self, list1: Optional[ListNode], list2: Optional[ListNode]) -> Optional[ListNode]:
        curr = ListNode()
        currSaved = curr

        while list1 and list2:
            if list1.val < list2.val:
                currSaved.next = list1
                list1 = list1.next
            else:
                currSaved.next = list2
                list2 = list2.next
            
            currSaved = currSaved.next
        
        if list1:
            currSaved.next = list1
        
        if list2:
            currSaved.next = list2
        
        return curr.next
