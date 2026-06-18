1class Solution:
2    def isAnagram(self, s: str, t: str) -> bool:
3        if len(s) != len(t):
4            return False
5        hash_s = {}
6        for char in s:
7            count = hash_s.get(char, 0)
8            hash_s[char] = count + 1
9        for val in t:
10            if val not in hash_s:
11                return False
12            hash_s[val] -= 1
13            if hash_s[val] < 0:
14                return False
15        return True