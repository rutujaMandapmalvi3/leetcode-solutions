1class Solution:
2    def isValidSudoku(self, board: List[List[str]]) -> bool:
3        cols = collections.defaultdict(set)
4        rows = collections.defaultdict(set)
5        square = collections.defaultdict(set)
6
7        for r in range(9):
8            for c in range(9):
9                if board[r][c] == ".":
10                    continue
11                if (board[r][c] in rows[r] or 
12                    board[r][c] in cols[c] or
13                    board[r][c] in square[r // 3, c // 3]):
14                    return False
15                rows[r].add(board[r][c])
16                cols[c].add(board[r][c])
17                square[r // 3, c // 3].add(board[r][c])
18        return True