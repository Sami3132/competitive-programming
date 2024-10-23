# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def replaceValueInTree(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([root])
        levelSum = []

        while queue:
            total = 0

            for _ in range(len(queue)):
                node = queue.popleft()
                total += node.val

                if node.left:
                    queue.append(node.left)
                
                if node.right:
                    queue.append(node.right)
            
            levelSum.append(total)
        
        queue = deque([(root, root.val)])
        level = 0

        while queue:
            for _ in range(len(queue)):
                node, val = queue.popleft()

                node.val = levelSum[level] - val

                childSum = 0

                if node.left:
                    childSum += node.left.val
                if node.right:
                    childSum += node.right.val
                if node.left:
                    queue.append((node.left, childSum))
                if node.right:
                    queue.append((node.right, childSum))
            
            level += 1
        
        return root
