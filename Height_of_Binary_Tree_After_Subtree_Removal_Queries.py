# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def treeQueries(self, R: Optional[TreeNode], Q: List[int]) -> List[int]:
        Depth, Height = collections.defaultdict(int), collections.defaultdict(int)

        def dfs(node, depth):
            if not node:
                return -1
            Depth[node.val] = depth
            cur = max(dfs(node.left, depth + 1), dfs(node.right, depth + 1)) + 1
            Height[node.val] = cur
            return cur

        dfs(R, 0)

        cousins = collections.defaultdict(list)

        for val, depth in Depth.items():
            cousins[depth].append((-Height[val], val))
            cousins[depth].sort()
            if len(cousins[depth]) > 2:
                cousins[depth].pop()

        ans = []
        for q in Q:
            depth = Depth[q]
            if len(cousins[depth]) == 1:
                ans.append(depth - 1)
            elif cousins[depth][0][1] == q:
                ans.append(-cousins[depth][1][0] + depth)
            else:
                ans.append(-cousins[depth][0][0] + depth)

        return ans
