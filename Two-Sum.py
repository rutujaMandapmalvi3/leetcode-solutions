1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3        '''        for i in range(len(nums)):
4            for j in range(i+1, len(nums)):
5                if nums[i] + nums[j] == target:
6                    return [i, j]'''
7
8        indices = {}
9        for i, val in enumerate(nums):    
10            indices[val] = i
11        for i, val in enumerate(nums):
12            diff = target - val
13            if diff in indices and indices[diff] != i:
14                print(indices[diff], i)
15                return[indices[diff], i]