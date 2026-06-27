1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def partition(self, head: Optional[ListNode], x: int) -> Optional[ListNode]:
8        left, right = ListNode(), ListNode()
9        leftTail, rightTail = left, right
10
11        while head:
12            if head.val < x:
13                leftTail.next = head
14                leftTail = leftTail.next
15            else:
16                rightTail.next = head
17                rightTail = rightTail.next
18            head = head.next
19
20        leftTail.next = right.next
21        rightTail.next = None
22        return left.next