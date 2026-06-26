1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def removeNthFromEnd(self, head: Optional[ListNode], n: int) -> Optional[ListNode]:
8        dummy = ListNode(0, head)
9        left = dummy
10        right = head
11
12        while n > 0 and right:
13            right = right.next
14            n -= 1
15        
16        while right:
17            right = right.next
18            left = left.next
19        
20        left.next = left.next.next
21
22        return dummy.next
23