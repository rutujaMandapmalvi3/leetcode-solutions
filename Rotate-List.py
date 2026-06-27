1# Definition for singly-linked list.
2# class ListNode:
3#     def __init__(self, val=0, next=None):
4#         self.val = val
5#         self.next = next
6class Solution:
7    def rotateRight(self, head: Optional[ListNode], k: int) -> Optional[ListNode]:
8        if not head or not head.next:
9            return head
10
11        left = head
12        length = 1
13        while left.next:
14            left = left.next
15            length += 1
16        
17        k = k % length 
18        if k == 0:
19            return head
20
21        curr = head    
22        for i in range(length - k -1):
23            curr = curr.next
24        newHead = curr.next
25        curr.next = None
26        left.next = head
27        return newHead