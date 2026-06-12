1class Solution:
2    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
3        res = []
4        left, right = 0, len(matrix[0])
5        top, bottom = 0, len(matrix)
6
7        while left < right and top < bottom:
8
9            for i in range(left, right):
10                res.append(matrix[top][i])
11            top += 1
12
13            for i in range(top, bottom):
14                res.append(matrix[i][right-1])
15            right -= 1
16
17            if not (left < right and top < bottom):
18                break
19
20            for i in range(right - 1, left - 1, -1):
21                res.append(matrix[bottom-1][i])
22            bottom -= 1
23
24            for i in range(bottom-1, top-1, -1):
25                res.append(matrix[i][left])
26            left += 1
27
28        return res