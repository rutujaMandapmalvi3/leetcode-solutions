1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def minDepth(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11
12        self.min_depth = float('inf')
13        self.dfs(root, 0)
14        return self.min_depth
15
16    def dfs(self, node, curr_depth):
17        if not node:
18            return
19
20        if not node.left and not node.right:
21            self.min_depth = min(self.min_depth, 1 + curr_depth)
22        
23        self.dfs(node.left, curr_depth+1)
24        self.dfs(node.right, curr_depth+1)
25        