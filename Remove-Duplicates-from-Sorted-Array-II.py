1class Solution:
2    def removeDuplicates(self, nums: List[int]) -> int:
3        k = 0
4        for i in range(len(nums)):
5            if k<2 or nums[i] != nums[k-2]:
6                nums[k] = nums[i]
7                k += 1
8        return k