1class Solution:
2    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
3        intervals.sort(key = lambda i : i[0])
4        output = [intervals[0]]
5        for start, end in intervals:
6            lastEnd = output[-1][1]
7            if start <= lastEnd:
8                output[-1][1] = max(lastEnd, end)
9            else:
10                output.append([start, end])
11        return output