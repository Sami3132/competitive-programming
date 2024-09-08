# Definition for singly-linked list.
# class ListNode:
#     def __init__(self, val=0, next=None):
#         self.val = val
#         self.next = next
class Solution:
    def splitListToParts(self, head: Optional[ListNode], k: int) -> List[Optional[ListNode]]:
        count = 0

        curr = head

        while curr:
            count += 1
            curr = curr.next
        
        div, rem = count // k, count % k
        curr = head
        ans = []

        for i in range(k):
            ans.append(curr)

            for j in range(div - 1 + (1 if rem else 0)):
                if not curr:
                    break
                curr = curr.next
            
            rem -= (1 if rem else 0)

            if curr:
                curr.next, curr = None, curr.next
        
        return ans
