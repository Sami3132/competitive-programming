# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def largestValues(self, root: Optional[TreeNode]) -> List[int]:
        if not root:
            return []
            
        queue = deque([root])
        ans = []

        while queue:
            maximum = float("-inf")
            
            for i in range(len(queue)):
                el = queue.popleft()
                maximum = max(maximum, el.val)

                if el.left:
                    queue.append(el.left)
                if el.right:
                    queue.append(el.right)
            
            ans.append(maximum)
        
        return ans
