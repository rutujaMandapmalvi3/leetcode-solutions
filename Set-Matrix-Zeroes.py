1class Solution:
2    def setZeroes(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        ROWS, COLS = len(matrix), len(matrix[0])
7        rowZero = False
8
9        for r in range(ROWS):
10            for c in range(COLS):
11                if matrix[r][c] == 0:
12                    matrix[0][c] = 0
13                    if r>0:
14                        matrix[r][0] = 0
15                    else:
16                        rowZero = True
17                
18        for r in range(1, ROWS):
19            for c in range(1, COLS):
20                if matrix[r][0] == 0 or matrix[0][c] == 0:
21                    matrix[r][c] = 0
22
23        if matrix[0][0] == 0:
24            for r in range(ROWS):
25                for c in range(COLS):
26                    matrix[r][0] = 0
27                    
28                    
29        if rowZero:
30            for c in range(COLS):
31                matrix[0][c] = 0
32            