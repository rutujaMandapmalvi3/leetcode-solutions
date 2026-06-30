1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxPathSum(self, root: Optional[TreeNode]) -> int:
9        res = [root.val]
10        def dfs(root):
11            if not root:
12                return 0
13            leftPathSum = dfs(root.left)
14            rightPathSum = dfs(root.right)
15            leftPathSum = max(leftPathSum, 0)
16            rightPathSum = max(rightPathSum, 0)
17            res[0] = max(res[0], (root.val + leftPathSum + rightPathSum))
18
19            return root.val + max(leftPathSum, rightPathSum)
20
21        dfs(root)
22        return res[0]