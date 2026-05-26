1class Solution:
2    def majorityElement(self, nums: List[int]) -> int:
3        # brute force:
4        '''        
5        counter = {}
6        max_appeared, half = 0, len(nums)/2
7
8        for i in nums:
9            counter[i] = 1 + counter.get(i, 0)
10            max_appeared = i if counter[i] > half else max_appeared
11        return max_appeared'''
12
13        # O(1):
14        max_appeared, count = 0, 0
15        for n in nums:
16            if count == 0:
17                max_appeared = n
18            count += (1 if max_appeared == n else -1)
19        return max_appeared