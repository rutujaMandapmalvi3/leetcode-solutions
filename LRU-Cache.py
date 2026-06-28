1class Node:
2    def __init__(self, key, val):
3        self.key = key
4        self.val = val
5        self.next = self.prev = None
6
7class LRUCache:
8
9    def __init__(self, capacity: int):
10        self.cap = capacity
11        self.cache = {}
12
13        self.right = self.left = Node(0, 0)
14        self.left.next = self.right
15        self.right.prev = self.left
16
17    def remove(self, node):
18        prev, next = node.prev, node.next
19        prev.next, next.prev = next, prev
20    
21    def insert(self, node):
22        prev, next = self.right.prev, self.right
23        node.prev = prev
24        node.next = next
25        prev.next = next.prev = node
26
27    def get(self, key: int) -> int:
28        if key in self.cache:
29            self.remove(self.cache[key])
30            self.insert(self.cache[key])
31            return self.cache[key].val
32        return -1
33
34    def put(self, key: int, value: int) -> None:
35        if key in self.cache:
36            self.remove(self.cache[key])
37        self.cache[key] = Node(key, value)
38        self.insert(self.cache[key])
39        
40        if len(self.cache) > self.cap:
41            lru = self.left.next
42            self.remove(lru)
43            del self.cache[lru.key]
44
45
46# Your LRUCache object will be instantiated and called as such:
47# obj = LRUCache(capacity)
48# param_1 = obj.get(key)
49# obj.put(key,value)