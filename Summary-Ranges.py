1class Solution:
2    def summaryRanges(self, nums: List[int]) -> List[str]:
3        numsSet = set(nums)
4        output = []
5
6        for n in nums:
7            if (n - 1) not in numsSet:
8                end = n
9                while (end + 1) in numsSet:
10                    end += 1
11                if end == n:
12                    output.append(str(n))
13                else:
14                    output.append(f"{n}->{end}")
15        return output