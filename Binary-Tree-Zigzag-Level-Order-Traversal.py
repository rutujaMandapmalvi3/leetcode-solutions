1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def zigzagLevelOrder(self, root: Optional[TreeNode]) -> List[List[int]]:
9        if not root:
10            return []
11        q = deque([root])
12        res = []
13        level_change = [0]
14        while q:
15            level_change[0] += 1
16            level = []
17            qLen = len(q)
18            for i in range(qLen):
19                node = q.popleft()
20                if node:
21                    level.append(node.val)
22                    if node.left:
23                        q.append(node.left)
24                    if node.right:
25                        q.append(node.right)
26            if level_change[0] % 2 == 0:
27                res.append(level[::-1])
28            else:
29                res.append(level)
30        return res