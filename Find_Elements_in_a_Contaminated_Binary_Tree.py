# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class FindElements:

    def __init__(self, root: Optional[TreeNode]):
        self.mySet = set()

        queue = deque([root])
        root.val = 0
        self.mySet.add(0)

        while queue:
            node = queue.popleft()

            if node.left:
                node.left.val = node.val * 2 + 1
                queue.append(node.left)
                self.mySet.add(node.left.val)
            if node.right:
                node.right.val = node.val * 2 + 2
                queue.append(node.right)
                self.mySet.add(node.right.val)

    def find(self, target: int) -> bool:
        return target in self.mySet
        


# Your FindElements object will be instantiated and called as such:
# obj = FindElements(root)
# param_1 = obj.find(target)
