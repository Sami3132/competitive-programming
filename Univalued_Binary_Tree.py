# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isUnivalTree(self, root: TreeNode) -> bool:

        def dfs(node: TreeNode) -> TreeNode:
            if node:
                yield node
                yield from dfs(node.left)
                yield from dfs(node.right)

        return all(node.val == root.val for node in dfs(root))
