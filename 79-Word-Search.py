class Solution:
    def exist(self, board: list[list[str]], word: str) -> bool:
        ROWS = len(board)
        COLS = len(board[0])
        visited = set()

        def dfs(r, c, curr_char):
            if curr_char == len(word):
                return True
            if (r<0 or c<0 or 
                r>=ROWS or c>=COLS or 
                word[curr_char] != board[r][c] or 
                (r, c) in visited):
                return False

            visited.add((r,c))
            res = (dfs(r + 1, c, curr_char + 1) or
                dfs(r - 1, c, curr_char + 1) or
                dfs(r, c + 1, curr_char + 1) or
                dfs(r, c - 1, curr_char + 1))
            visited.remove((r,c))
            return res

        for r in range(ROWS):
            for c in range(COLS):
                if dfs(r, c, 0):
                    return True
        return False