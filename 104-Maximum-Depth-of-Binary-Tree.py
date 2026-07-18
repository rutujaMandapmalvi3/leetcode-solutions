# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def maxDepth(self, root: Optional[TreeNode]) -> int:
        '''
        if not root:
            return 0
        return 1 + max(self.maxDepth(root.left), self.maxDepth(root.right))'''

        '''if not root:
            return 0
        stk = [[root, 1]]
        res = 1
        while stk:
            node, depth = stk.pop()
            if node:
                res = max(res, depth)
                stk.append([node.right, depth + 1])
                stk.append([node.left, depth + 1])
        return res'''

        if not root:
            return 0

        left_max = self.maxDepth(root.left)
        right_max = self.maxDepth(root.right)
        
        return 1 + max(left_max, right_max)