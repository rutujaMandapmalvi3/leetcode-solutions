1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def isSymmetric(self, root: Optional[TreeNode]) -> bool:
9        def dfs(left, right):
10            if not left and not right:
11                return True
12            if not left or not right:
13                return False
14            return (left.val == right.val and dfs(left.left, right.right) and dfs(left.right, right.left))
15        return dfs(root.left, root.right)