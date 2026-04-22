1class Solution:
2    def generate(self, numRows: int) -> List[List[int]]:
3        res = [[1]]
4        for i in range(numRows - 1):
5            temp = [0] + res[-1] + [0]
6            row = []
7            for j in range(len(res[-1]) + 1):
8                row.append(temp[j] + temp[j + 1])
9            res.append(row)
10        return res