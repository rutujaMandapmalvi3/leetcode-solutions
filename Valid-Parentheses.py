1class Solution:
2    def isValid(self, s: str) -> bool:
3        s_hash = {')':'(',
4                 ']': '[',
5                 '}':'{'}
6        stack = []
7        for c in s:
8            if c in s_hash and stack and stack[-1] == s_hash[c]:
9                stack.pop()
10            else:
11                stack.append(c)
12        return True if not stack else False