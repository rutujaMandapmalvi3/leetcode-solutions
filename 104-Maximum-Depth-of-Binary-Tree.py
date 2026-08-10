# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: TreeNode) -> int:
        '''def recursive(root):
            if root == None:
                return 0

            return max(recursive(root.left)+1,recursive(root.right)+1)

        return recursive(root)'''

        if root is None:
            return 0
        return 1 + max(self.maxDepth(root.right), self.maxDepth(root.left))
                    
                



            