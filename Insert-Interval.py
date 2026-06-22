1class Solution:
2    def insert(self, intervals: List[List[int]], newInterval: List[int]) -> List[List[int]]:
3        output = []
4        for i, (start, end) in enumerate(intervals):
5            if end < newInterval[0]:
6                output.append([start, end])
7            elif start > newInterval[1]:
8                output.append(newInterval)
9                output.extend(intervals[i:])
10                return output
11            else:
12                newInterval[0] = min(start, newInterval[0])
13                newInterval[1] = max(end, newInterval[1])
14        output.append(newInterval)
15        return output