1class Solution:
2    def convert(self, s: str, numRows: int) -> str:
3        if numRows == 1:
4            return s
5
6        i = 0
7        d = 1
8        rows = [[] for _ in range(numRows)]
9
10        for char in s:
11            rows[i].append(char)
12            if i == 0:
13                d = 1
14            elif i == numRows - 1:
15                d = -1
16            i += d
17
18        ret = ''
19        for i in range(numRows):
20            ret += ''.join(rows[i])
21        return ret