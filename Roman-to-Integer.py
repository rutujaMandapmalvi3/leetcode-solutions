1class Solution:
2    def romanToInt(self, s: str) -> int:
3        s_hash = {
4            'I': 1, 'V': 5, 'X':10, 'L':50, 'C':100, 'D':500, 'M':1000
5        }
6        total = 0
7        for i in range(len(s)-1):
8            if s_hash[s[i]] < s_hash[s[i+1]]:
9                total -= s_hash[s[i]]
10            else:
11                total += s_hash[s[i]]
12        total += s_hash[s[-1]]
13        return total