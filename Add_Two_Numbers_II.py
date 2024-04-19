# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def addTwoNumbers(self, l1: Optional[ListNode], l2: Optional[ListNode]) -> Optional[ListNode]:
        list1 = l1
        list2 = l2

        prev = None

        while list1:
            next = list1.next
            list1.next = prev
            prev = list1
            list1 = next
        
        list1 = prev
        
        prev = None

        while list2:
            next = list2.next
            list2.next = prev
            prev = list2
            list2 = next
        
        list2 = prev

        carry = 0
        newNode = ListNode(0)
        mainNode = newNode

        while list1 or list2:
            val1 = list1.val if list1 else 0
            val2 = list2.val if list2 else 0

            total = val1 + val2 + carry

            carry = floor(total / 10)

            mainNode.next = ListNode(total % 10)
            mainNode = mainNode.next
            
            if list1:
                list1 = list1.next

            if list2:
                list2 = list2.next
            
        
        if carry == 1:
            mainNode.next = ListNode(1)

        newNode = newNode.next
        list3 = newNode
        prev = None

        while list3:
            next = list3.next
            list3.next = prev
            prev = list3
            list3 = next
        
        list3 = prev
        
        return list3
