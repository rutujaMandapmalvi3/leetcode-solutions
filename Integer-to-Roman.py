1class Solution:
2    def intToRoman(self, num: int) -> str:
3        symList = [['I', 1], ['IV', 4], ['V', 5], ['IX', 9], ['X', 10], ['XL', 40], ['L', 50], ['XC', 90], ['C', 100], ['CD', 400], ['D', 500], ['CM', 900], ['M', 1000]]
4 
5        res = ''
6        for sym, val in reversed(symList):
7            if num // val:
8                count = num // val
9                res += count * sym
10                num = num % val
11        return res