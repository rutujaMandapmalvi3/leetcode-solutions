1class Solution:
2    def solve(self, board: List[List[str]]) -> None:
3        """
4        Do not return anything, modify board in-place instead.
5        """
6        rows, cols = len(board), len(board[0])
7        def capture(r, c):
8            if ((r not in range(rows)) or (r > rows -1) or (c not in range(cols)) or (c > cols -1) or board[r][c] != "O"):
9                return
10            board[r][c] = "T"
11            capture(r + 1, c)
12            capture(r - 1, c)
13            capture(r, c + 1)
14            capture(r, c - 1)
15
16        for r in range(rows):
17            for c in range(cols):
18                if (board[r][c] == "O" and (r in [0, rows - 1]) or (c in [0, cols - 1])):
19                    capture(r, c)
20        
21        for r in range(rows):
22            for c in range(cols):
23                if board[r][c] == "O":
24                    board[r][c] = "X"
25        
26        for r in range(rows):
27            for c in range(cols):
28                if board[r][c] == "T":
29                    board[r][c] = "O"