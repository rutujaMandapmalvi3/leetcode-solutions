1from collections import defaultdict
2class Solution:
3    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
4        res = defaultdict(list)
5        for i in strs:
6            count = [0] * 26
7            for j in i:
8                count[ord(j) - ord('a')] += 1
9            res[tuple(count)].append(i)
10        return list(res.values())