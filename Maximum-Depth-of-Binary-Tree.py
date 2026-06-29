1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def maxDepth(self, root: Optional[TreeNode]) -> int:
9        '''
10        if not root:
11            return 0
12        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))'''
13
14        if not root:
15            return 0
16        stk = [[root, 1]]
17        res = 1
18        while stk:
19            node, depth = stk.pop()
20            if node:
21                res = max(res, depth)
22                stk.append([node.right, depth + 1])
23                stk.append([node.left, depth + 1])
24        return res