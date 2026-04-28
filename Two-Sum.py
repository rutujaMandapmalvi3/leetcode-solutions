1class Solution:
2    def twoSum(self, nums: List[int], target: int) -> List[int]:
3'''        for i in range(len(nums)-1):
4            for j in range(i+1, len(nums)):
5                if nums[i] + nums[j] == target and [i] != [j]:
6                    return ([i, j])'''
7
8    numshash = {}
9    for i in enumerate(numshash):
10        numshash[val] = i
11    for i in enumerate(numshash):
12        diff = target - val
13        if diff in numshash and numshash[val] != i:
14            return numshash[i, diff[val]]