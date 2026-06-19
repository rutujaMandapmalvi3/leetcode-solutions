1class Solution:
2    def longestConsecutive(self, nums: List[int]) -> int:
3        numSet = set(nums)
4        longest = 0
5
6        for n in numSet:
7            if (n - 1) not in numSet:
8                count = 0
9                while (n + count) in numSet:
10                    count += 1
11                longest = max(longest, count)
12        return longest