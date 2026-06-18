1class Solution:
2    def wordPattern(self, pattern: str, s: str) -> bool:
3        mapPS = {}
4        mapSP = {}
5        words = s.split()
6
7        if len(pattern) != len(words):
8            return False
9
10        for i, j in zip(pattern, words):
11            if ((i in mapPS and mapPS[i] != j) or (j in mapSP and mapSP[j] != i)):
12                return False
13            mapPS[i] = j
14            mapSP[j] = i
15        return True
16                