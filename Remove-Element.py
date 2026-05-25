1class Solution:
2    def removeElement(self, nums: List[int], val: int) -> int:
3        k = 0
4        for i in range(len(nums)):
5            if nums[i] != val:
6                nums[k] = nums[i]
7                k += 1
8        return k