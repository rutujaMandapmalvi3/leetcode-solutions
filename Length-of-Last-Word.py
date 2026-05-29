1class Solution:
2    def lengthOfLastWord(self, s: str) -> int:
3        count = 0
4        for i in range(len(s)-1, -1, -1):
5            if count == 0 and s[i] == ' ':
6                continue
7            if s[i] == ' ':
8                return count
9            count += 1
10        return count