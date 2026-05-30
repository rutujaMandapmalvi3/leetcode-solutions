1class Solution:
2    def reverseWords(self, s: str) -> str:
3        s_reverse = s.split()
4        left = 0
5        right = len(s_reverse) - 1
6        
7        while left < right:
8            s_reverse[left], s_reverse[right] = s_reverse[right], s_reverse[left]
9
10            left += 1
11            right -= 1
12
13        return " ".join(s_reverse)