# Definition for a binary tree node.
# class TreeNode:
#     def __init__(self, val=0, left=None, right=None):
#         self.val = val
#         self.left = left
#         self.right = right
class Solution:
    def isBalanced(self, root: Optional[TreeNode]) -> bool:
        # flag = [True]
        # def dfs(root):
        #     if root == None:
        #         return 0

        #     left = dfs(root.left)
        #     right = dfs(root.right)

        #     # print(left)
        #     # print(right)
        #     # print('------')
        #     if abs(left - right)>1:
        #         flag[0] = False


        #     return max(left,right) + 1
        # dfs(root)
        # return flag[0]
        '''flag = [True]
        def dfs(root):
            if not root:
                return 0, flag[0]

            left, f_l = dfs(root.left)
            right,f_r = dfs(root.right)

            if abs(left - right) > 1:
                flag[0] = False

            return max(right,left) + 1, flag[0]

        l,f = dfs(root) 
        return f '''
        flag = [True]
        def dfs(root):
            if not root:
                return 0, flag[0]
            left, f_l = dfs(root.left)
            right, f_r = dfs(root.right)
            if abs(left - right) > 1:
                flag[0] = False
            return max(left, right) + 1, flag[0]
        height, return_flag = dfs(root)
        return return_flag
        

    