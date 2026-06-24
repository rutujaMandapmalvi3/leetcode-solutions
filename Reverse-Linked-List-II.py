1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def reverseBetween(self, head: Optional[ListNode], left: int, right: int) -> Optional[ListNode]:
8
9        dummy = ListNode(0, head)
10        leftPrev, curr = dummy, head
11
12        for i in range(left-1):
13            leftPrev = curr
14            curr = curr.next
15
16        prev = None
17        for i in range(right - left + 1):
18            temp = curr.next
19            curr.next = prev
20            prev, curr = curr, temp
21
22        leftPrev.next.next = curr
23        leftPrev.next = prev
24        return dummy.next