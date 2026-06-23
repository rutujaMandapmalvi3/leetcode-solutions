1class MinStack:
2
3    def __init__(self):
4        self.stack = []
5        self.minstack = []
6
7    def push(self, value: int) -> None:
8        self.stack.append(value)
9        value = min(value, self.minstack[-1] if self.minstack else value)
10        self.minstack.append(value)
11
12    def pop(self) -> None:
13        self.stack.pop()
14        self.minstack.pop()
15
16    def top(self) -> int:
17        return self.stack[-1]
18
19    def getMin(self) -> int:
20        return self.minstack[-1]
21
22
23# Your MinStack object will be instantiated and called as such:
24# obj = MinStack()
25# obj.push(value)
26# obj.pop()
27# param_3 = obj.top()
28# param_4 = obj.getMin()