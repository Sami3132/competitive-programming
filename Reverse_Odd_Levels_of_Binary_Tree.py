# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right

class Solution:
    def reverseOddLevels(self, root: Optional[TreeNode]) -> Optional[TreeNode]:
        queue = deque([(root, 0)])
        
        while queue:
            levelNodes = []
            level = queue[0][1]

            for _ in range(len(queue)):
                node, currLevel = queue.popleft()
                levelNodes.append(node)
                
                if node.left:
                    queue.append((node.left, currLevel + 1))
                    queue.append((node.right, currLevel + 1))
            
            if level % 2 == 1:
                i, j = 0, len(levelNodes) - 1
                
                while i < j:
                    levelNodes[i].val, levelNodes[j].val = levelNodes[j].val, levelNodes[i].val
                    i += 1
                    j -= 1

        return root
