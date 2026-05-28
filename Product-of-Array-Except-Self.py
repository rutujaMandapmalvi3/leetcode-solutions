1class Solution:
2    def productExceptSelf(self, nums: List[int]) -> List[int]:
3        prefix = 1
4        postfix = 1
5        output = [1] * (len(nums))
6
7        for i in range(len(nums)):
8            output[i] = prefix
9            prefix *= nums[i]
10        for i in range(len(nums) - 1, -1, -1):
11            output[i] *= postfix
12            postfix *= nums[i]
13        return output