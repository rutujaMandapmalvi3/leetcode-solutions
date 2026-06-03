1class Solution:
2    def twoSum(self, numbers: List[int], target: int) -> List[int]:
3
4        l, r = 0, len(numbers) - 1
5        while l<r:
6            arr_add = numbers[l] + numbers[r]
7            if arr_add == target:
8                return [l+1, r+1]
9            elif arr_add < target:
10                l += 1
11            else:
12                r -= 1
13
14        return 0