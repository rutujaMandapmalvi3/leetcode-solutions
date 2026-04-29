1class Solution:
2    def isPalindrome(self, x: int) -> bool:
3        x = str(x)
4        l, r = 0, len(x)-1
5        while l <= r:
6            if x[l] != x[r]:
7                return False
8            l += 1
9            r -= 1   
10        return True