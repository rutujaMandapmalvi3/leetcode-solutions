1class Solution:
2    def longestConsecutive(self, nums: list[int]) -> int:
3        nums_sort = sorted(set(nums))
4        count = 1
5        max_count = 1
6        #result = []
7        if not nums:
8            return 0
9        print(nums_sort)
10        for i in range(1, len(nums_sort)):
11            if nums_sort[i] == nums_sort[i-1] + 1:
12                count += 1
13            else:
14                max_count = max(max_count, count)
15                count = 1
16        max_count = max(max_count, count)
17        return max_count