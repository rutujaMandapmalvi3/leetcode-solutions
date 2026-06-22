1class Solution:
2    def findMinArrowShots(self, points: List[List[int]]) -> int:
3        points.sort(key = lambda i : i[1])
4        arrows = 1
5        arrowPos = points[0][1]
6
7        for start, end in points[1:]:
8            if start > arrowPos:
9                arrows += 1
10                arrowPos = end
11        return arrows