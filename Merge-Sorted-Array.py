1class Solution:
2    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
3        """
4        Do not return anything, modify nums1 in-place instead.
5        """
6        last = m+n-1
7        while m>0 and n>0:
8            if nums1[m - 1] > nums2[n - 1]:
9                nums1[last] = nums1[m - 1]
10                m -= 1
11            else:
12                nums1[last] = nums2[n - 1]
13                n -= 1
14            last -= 1
15        while n>0:
16            nums1[last] = nums2[n - 1]
17            n, last = n-1, last-1
18        return nums1
19        