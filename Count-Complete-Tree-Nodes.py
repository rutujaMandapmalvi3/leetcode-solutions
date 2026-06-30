1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class Solution:
8    def countNodes(self, root: Optional[TreeNode]) -> int:
9        if not root:
10            return 0
11        
12        '''stack = []
13        count = 0
14        curr = root
15        while curr or stack:
16            while curr:
17                stack.append(curr)
18                curr = curr.left
19                
20            curr = stack.pop()
21            count += 1
22            curr = curr.right
23        return count'''
24
25        leftCount = self.countNodes(root.left)
26        rightCount = self.countNodes(root.right)
27        return 1 + leftCount + rightCount