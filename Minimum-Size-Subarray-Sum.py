1class Solution:
2    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
3        l, total = 0, 0
4        min_length = float("inf")
5        for r in range(len(nums)):
6            total += nums[r]
7            while total >= target:
8                min_length = min(min_length, r - l + 1)
9                total -= nums[l]
10                l += 1
11        return 0 if min_length == float("inf") else min_length
12