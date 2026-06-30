1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.left = None
6#         self.right = None
7
8class Solution:
9    def lowestCommonAncestor(self, root: 'TreeNode', p: 'TreeNode', q: 'TreeNode') -> 'TreeNode':
10        parent = {root:None}
11        stack = [root]
12        while stack:
13            node = stack.pop()
14            if node.left:
15                parent[node.left] = node
16                stack.append(node.left)
17            if node.right:
18                parent[node.right] = node
19                stack.append(node.right)
20        ancestors = set()
21        while p:
22            ancestors.add(p)
23            p = parent[p]
24        while not q in ancestors:
25            q = parent[q]
26        
27        return q