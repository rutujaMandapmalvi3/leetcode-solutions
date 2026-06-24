1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, x):
4#         self.val = x
5#         self.next = None
6
7class Solution:
8    def hasCycle(self, head: Optional[ListNode]) -> bool:
9
10
11        slow, fast = head, head
12        while fast and fast.next:
13            slow = slow.next
14            fast = fast.next.next
15            if slow == fast:
16                return True
17        return False