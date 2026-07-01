1from collections import deque
2# Definition for a binary tree node.
3# class TreeNode:
4#     def __init__(self, val=0, left=None, right=None):
5#         self.val = val
6#         self.left = left
7#         self.right = right
8class Solution:
9    def isValidBST(self, root: Optional[TreeNode]) -> bool:
10        q = deque([(root, float('-inf'), float('inf'))])
11        while q:
12            node, low, high = q.popleft()
13            if node.val <= low or node.val >= high:
14                return False
15            if node.left:
16                q.append((node.left, low, node.val))
17            if node.right:
18                q.append((node.right, node.val, high))
19        return True