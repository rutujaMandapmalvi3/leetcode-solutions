1class Solution:
2    def convert(self, s: str, numRows: int) -> str:
3        if numRows == 1:
4            return s
5        res = ""
6        for r in range(numRows):
7            increment = 2 * (numRows - 1)
8            for i in range(r, len(s), increment):
9                res += s[i]
10                if (r>0 and r<numRows - 1 and i + increment - 2 * r < len(s)):
11                    res += s[i + increment - 2*r]
12        return res