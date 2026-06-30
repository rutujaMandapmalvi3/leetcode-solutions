1from collections import deque
2# Definition for a binary tree node.
3# class TreeNode:
4#     def __init__(self, val=0, left=None, right=None):
5#         self.val = val
6#         self.left = left
7#         self.right = right
8class Solution:
9    def rightSideView(self, root: Optional[TreeNode]) -> List[int]:
10        res = []
11        q = deque([root])
12        while q:
13            qLen = len(q)
14            rightMost = None
15            for i in range(qLen):
16                node = q.popleft()
17                if node: 
18                    rightMost = node
19                    q.append(node.left)
20                    q.append(node.right)
21            if rightMost:
22                res.append(rightMost.val)
23        return res