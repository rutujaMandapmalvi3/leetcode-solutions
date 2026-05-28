1class RandomizedSet:
2
3    def __init__(self):
4        self.numsList = []
5        self.numsMap = {}
6
7    def insert(self, val: int) -> bool:
8        res = val not in self.numsMap
9        if res:
10            self.numsMap[val] = len(self.numsList)
11            self.numsList.append(val)
12        return res
13
14    def remove(self, val: int) -> bool:
15        res = val in self.numsMap
16        if res:
17            idx = self.numsMap[val]
18            lastval = self.numsList[-1]
19            self.numsList[idx] = lastval
20            self.numsList.pop()
21            self.numsMap[lastval] = idx
22            del self.numsMap[val]
23        return res
24
25    def getRandom(self) -> int:
26        return random.choice(self.numsList)
27
28
29# Your RandomizedSet object will be instantiated and called as such:
30# obj = RandomizedSet()
31# param_1 = obj.insert(val)
32# param_2 = obj.remove(val)
33# param_3 = obj.getRandom()