1# Definition for a binary tree node.
2# class TreeNode:
3#     def __init__(self, val=0, left=None, right=None):
4#         self.val = val
5#         self.left = left
6#         self.right = right
7class BSTIterator:
8
9    def __init__(self, root: Optional[TreeNode]):
10        self.stack = []
11        curr = root
12        while curr:
13            self.stack.append(curr)
14            curr = curr.left
15
16    def next(self) -> int:
17        res = self.stack.pop()
18
19        curr = res.right
20        while curr:
21            self.stack.append(curr)
22            curr = curr.left
23        return res.val
24
25    def hasNext(self) -> bool:
26        return self.stack != []
27
28
29# Your BSTIterator object will be instantiated and called as such:
30# obj = BSTIterator(root)
31# param_1 = obj.next()
32# param_2 = obj.hasNext()