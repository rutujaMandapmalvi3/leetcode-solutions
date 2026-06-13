1class Solution:
2    def isIsomorphic(self, s: str, t: str) -> bool:
3        mapST = {}
4        mapTS = {}
5        
6        if len(s) != len(t):
7            return False
8        for c1, c2 in zip(s, t):
9            if ((c1 in mapST and mapST[c1] != c2) or (c2 in mapTS and mapTS[c2] != c1)):
10                return False
11            mapST[c1] = c2
12            mapTS[c2] = c1
13        return True