1class Solution:
2    def longestCommonPrefix(self, strs: List[str]) -> str:
3        res = ""
4        for i in range(len(strs[0])):
5            for s in strs:
6                if i == len(s) or s[i] != strs[0][i]:
7                    return res
8            res += strs[0][i]
9        return res