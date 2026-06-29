1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
9        
10        inorderIdx = {val:i for i, val in enumerate(inorder)}
11        
12        
13        def helper(l, r):
14            if l > r:
15                return None
16            root = TreeNode(postorder.pop())
17            idx = inorderIdx[root.val]
18            root.right = helper(idx + 1, r)
19            root.left = helper(l, idx-1)
20            return root
21        return helper(0, len(inorder)- 1)