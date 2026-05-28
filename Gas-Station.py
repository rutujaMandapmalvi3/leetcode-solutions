1class Solution:
2    def canCompleteCircuit(self, gas: List[int], cost: List[int]) -> int:
3        if sum(gas) < sum(cost):
4            return -1
5        total = 0
6        starting_pos = 0
7
8        for i in range(len(gas)):
9            total += (gas[i] - cost[i])
10            if total < 0:
11                total = 0
12                starting_pos = i + 1
13        return starting_pos