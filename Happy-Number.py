1class Solution:
2    def isHappy(self, n: int) -> bool:
3        slow, fast = n, self.sqr_n(n)
4        while fast != 1 and slow != fast:
5            slow = self.sqr_n(slow)
6            fast = self.sqr_n(self.sqr_n(fast))
7        return fast == 1
8
9    def sqr_n(self, x):
10        total = 0
11        for i in str(x):
12            total += int(i) * int(i)
13        return total