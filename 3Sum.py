1class Solution:
2    def threeSum(self, nums: list[int]) -> list[list[int]]:
3        res = []
4        nums.sort() # nums = [-1, -1, 0, 1, 2, 4]
5        for i, val in enumerate(nums):
6            if i > 0 and val == nums[i - 1]:
7                continue
8            l, r = i + 1, len(nums) - 1
9            while l < r:
10                sums = val + nums[l] + nums[r]
11                if sums > 0:
12                    r -= 1
13                elif sums < 0:
14                    l += 1
15                else:
16                    res.append([val, nums[l], nums[r]])
17                    l += 1
18                    while nums[l] == nums[l - 1] and l < r:
19                        l += 1 
20        return res