1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        prefix = strs[0]
4        for i in strs[1:]:
5            while not i.startswith(prefix):
6                prefix = prefix[:-1]
7        return prefix