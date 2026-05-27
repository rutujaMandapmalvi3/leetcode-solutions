1class Solution:
2    def rotate(self, nums: List[int], k: int) -> None:
3        """
4        Do not return anything, modify nums in-place instead.
5        """
6        k = k % len(nums)
7        l, r = 0, len(nums) - 1
8        while l<r:
9            nums[l], nums[r] = nums[r], nums[l]
10            r-= 1
11            l+= 1
12        
13        l, r = 0, k-1
14        while l<r:
15            nums[l], nums[r] = nums[r], nums[l]
16            r-= 1
17            l+= 1
18        
19        l, r = k, len(nums) - 1
20        while l<r:
21            nums[l], nums[r] = nums[r], nums[l]
22            r-= 1
23            l+= 1