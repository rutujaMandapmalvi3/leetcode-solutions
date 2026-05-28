1class Solution:
2    def jump(self, nums: List[int]) -> int:
3        jumps = 0
4        l = r = 0
5        while r < len(nums) - 1:
6            farthest = 0
7            for i in range(l, r+1):
8                farthest = max(farthest, i + nums[i])
9            l = r+1
10            r = farthest
11            jumps += 1
12        return jumps
13            
14            
15
16