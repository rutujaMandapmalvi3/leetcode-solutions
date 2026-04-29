1class Solution:
2    def romanToInt(self, s: str) -> int:
3        hashRoman = {'I':1,
4                    'V':5,
5                    'X':10,
6                    'L':50,
7                    'C':100,
8                    'D':500,
9                    'M':1000}
10
11        total = 0
12        for i in range(len(s)-1):
13            if hashRoman[s[i]] < hashRoman[s[i+1]]:
14                print(hashRoman[s[i]])
15                total -= hashRoman[s[i]]
16                print("total_up = ", total)
17            else:
18                print(i, hashRoman[s[i]])
19                total += hashRoman[s[i]]
20                print("total = ", total)
21        total += hashRoman[s[-1]]
22        return total