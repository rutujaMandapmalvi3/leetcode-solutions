1class Solution:
2    def findOrder(self, numCourses: int, prerequisites: List[List[int]]) -> List[int]:
3        preMap = {i:[] for i in range(numCourses)}
4        for crs, pre in prerequisites:
5            preMap[crs].append(pre)
6        visited = set()
7        cycle = set()
8        output = []
9        def dfs(crs):
10            if crs in cycle:
11                return False
12            if crs in visited:
13                return True
14            cycle.add(crs)
15            for pre in preMap[crs]:
16                if not dfs(pre): return False
17            cycle.remove(crs)
18            visited.add(crs)
19            output.append(crs)
20            return True
21        for c in range(numCourses):
22            if not dfs(c): return []
23        return output