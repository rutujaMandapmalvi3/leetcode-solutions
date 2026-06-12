1class Solution:
2    def rotate(self, matrix: List[List[int]]) -> None:
3        """
4        Do not return anything, modify matrix in-place instead.
5        """
6        l, r = 0, len(matrix) - 1
7        while l < r:
8            for i in range(r-l):
9                top, bottom = l, r
10
11                tempLeft = matrix[top][l+i]
12                matrix[top][l+i] = matrix[bottom - i][l]
13                matrix[bottom - i][l] = matrix[bottom][r - i]
14                matrix[bottom][r - i] = matrix[top + i][r]
15                matrix[top + i][r] = tempLeft
16            l += 1
17            r -= 1