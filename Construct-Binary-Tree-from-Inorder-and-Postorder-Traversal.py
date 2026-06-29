1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def buildTree(self, inorder: List[int], postorder: List[int]) -> Optional[TreeNode]:
9        if not inorder:
10            return None
11        root = TreeNode(postorder.pop())
12        idx = inorder.index(root.val)
13        root.right = self.buildTree(inorder[idx + 1:], postorder)
14        root.left = self.buildTree(inorder[:idx], postorder)
15        return root