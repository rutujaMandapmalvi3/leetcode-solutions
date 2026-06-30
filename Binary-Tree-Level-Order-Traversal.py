1from collections import deque
2# Definition for a binary tree node.
3# class TreeNode:
4#     def __init__(self, val=0, left=None, right=None):
5#         self.val = val
6#         self.left = left
7#         self.right = right
8class Solution:
9    def levelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
10        if not root:
11            return []
12        q = deque([root])
13        res = []
14        while q:
15            level = []
16            qLen = len(q)
17            for i in range(qLen):
18                node = q.popleft()
19                if node:
20                    level.append(node.val)
21                    if node.left:
22                        q.append(node.left)
23                    if node.right:
24                        q.append(node.right)
25            print(level)
26            res.append(level)
27        return res