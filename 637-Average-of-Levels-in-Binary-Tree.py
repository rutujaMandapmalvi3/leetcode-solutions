from collections import deque
# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def averageOfLevels(self, root: TreeNode | None) -> list[float]:
        q = deque([root])
        avg_array = []
        while q:
            level_length = len(q)
            level_sum = 0
            for _ in range(level_length):
                node = q.popleft()
                level_sum += node.val

                if node.left:
                    q.append(node.left)
            
                if node.right:
                    q.append(node.right)
                
            avg_array.append(level_sum/level_length)
        return avg_array