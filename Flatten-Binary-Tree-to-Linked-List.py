1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def flatten(self, root: Optional[TreeNode]) -> None:
9        """
10        Do not return anything, modify root in-place instead.
11        """
12        
13        def dfs(root):
14            if not root:
15                return None
16            leftTail = dfs(root.left)
17            rightTail = dfs(root.right)
18
19            if root.left:
20                leftTail.right = root.right
21                root.right = root.left
22                root.left = None
23            last = rightTail or leftTail or root
24            return last
25        dfs(root)