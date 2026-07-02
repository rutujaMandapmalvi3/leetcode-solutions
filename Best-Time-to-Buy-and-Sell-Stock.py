1class Solution:
2    def maxProfit(self, prices: List[int]) -> int:
3        '''l, r = 0, 1
4        maxP = 0
5        while r < len(prices):
6            if prices[l] < prices[r]:
7                profit = prices[r] - prices[l]
8                maxP = max(maxP, profit)
9            else:
10                l = r
11            r += 1
12        return maxP'''
13
14        l, r = 0, 1
15        maxP = 0
16        while r < len(prices): 
17            if prices[r] < prices[l]:
18                l = r
19            maxP = max(maxP, prices[r] - prices[l])
20            r += 1
21            
22        return maxP