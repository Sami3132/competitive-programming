class Solution:
    def verticalTraversal(self, root: Optional[TreeNode]) -> List[List[int]]:
        myDict = defaultdict(list)
        
        def dfs(node, col, row):
            if not node:
                return
            
            heapq.heappush(myDict[col], (row, node.val))

            dfs(node.left, col - 1, row + 1)
            dfs(node.right, col + 1, row + 1)

        dfs(root, 0, 0)

        ans = []
        for key in sorted(myDict):
            colVals = []
            while myDict[key]:
                colVals.append(heapq.heappop(myDict[key])[1])
            ans.append(colVals)
        
        return ans
