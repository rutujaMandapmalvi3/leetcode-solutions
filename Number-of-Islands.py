1from collections import deque
2class Solution:
3    def numIslands(self, grid: List[List[str]]) -> int:
4        if not grid:
5            return 0
6        row, col = len(grid), len(grid[0])
7        visited = set()
8        island = 0
9
10        def bfs(r, c):
11            q = deque()
12            visited.add((r, c))
13            q.append((r, c))
14
15            while q:
16                curr_r, curr_c = q.pop()
17                dirs = [[1,0],[-1,0],[0,1], [0, -1]]
18
19                for dirs_r, dirs_c in dirs:
20                    nr, nc = dirs_r + curr_r, dirs_c + curr_c
21                    if nr in range(row) and nc in range(col) and grid[nr][nc] == "1" and (nr, nc) not in visited:
22                        q.append((nr, nc))
23                        visited.add((nr, nc))
24
25        for r in range(row):
26            for c in range(col):
27                if grid[r][c] == "1" and (r, c) not in visited:
28                    bfs(r, c)
29                    island += 1
30        return island