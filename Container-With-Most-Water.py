1class Solution:
2    def maxArea(self, height: List[int]) -> int:
3        l, r = 0, len(height) - 1
4        area = 0
5        while l < r:
6            maxArea = (r - l) * min(height[l], height[r])
7            area = max(area, maxArea)
8            if height[l] > height[r]:
9                r -= 1
10            else:
11                l += 1
12        return area