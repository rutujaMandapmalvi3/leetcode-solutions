1class Solution:
2    def isHappy(self, n: int) -> bool:
3        visit = set()
4
5        while n not in visit:
6            visit.add(n)
7            n = self.sqr_n(n)
8            if n == 1:
9                return True
10            
11        return False
12    
13    def sqr_n(self, n):
14        output = 0
15        while n:
16            digit = n % 10
17            digit = digit ** 2
18            output += digit
19            n = n // 10
20        return output