# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def recoverFromPreorder(self, traversal: str) -> Optional[TreeNode]:
        dashes = 0
        stack = []

        i = 0

        while i < len(traversal):
            while traversal[i] == '-':
                dashes += 1
                i += 1
            else:
                val = ""
                while i < len(traversal) and traversal[i] != '-':
                    val += traversal[i]
                    i += 1
                
                node = TreeNode(int(val))

                while len(stack) > dashes:
                    stack.pop()
                
                if stack and not stack[-1].left:
                    stack[-1].left = node
                elif stack:
                    stack[-1].right = node
                
                stack.append(node)
                
                dashes = 0
            print(stack)
        return stack[0]
