1class Solution:
2    def lengthOfLongestSubstring(self, s: str) -> int:
3        max_len = 0
4        l = 0
5        hash_s = {}
6        for r in range(len(s)):
7            if s[r] in hash_s and hash_s[s[r]] >= l:
8                l = hash_s[s[r]] + 1
9            hash_s[s[r]] = r
10            max_len = max(max_len, r - l + 1)
11        return max_len