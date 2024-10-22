# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def kthLargestLevelSum(self, root: Optional[TreeNode], k: int) -> int:
        nodes = deque([(root, 0)])
        level = total = 0
        levelTotal = []

        while nodes:
            node, currLevel = nodes.popleft()

            if level != currLevel:
                levelTotal.append(total)
                total = node.val
                level = currLevel
            else:
                total += node.val
            
            if node.left:
                nodes.append((node.left, currLevel + 1))
            
            if node.right:
                nodes.append((node.right, currLevel + 1))
        
        levelTotal.append(total)
        
        if len(levelTotal) < k:
            return -1
        
        levelTotal.sort()

        return levelTotal[-k]
