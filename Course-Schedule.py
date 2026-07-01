1class Solution:
2    def canFinish(self, numCourses: int, prerequisites: List[List[int]]) -> bool:
3        preMap = {i:[] for i in range(numCourses)}
4        for crs, pre in prerequisites:
5            preMap[crs].append(pre)
6        visited = set()
7        
8        def dfs(crs):
9            if preMap[crs] == []:
10                return True
11            if crs in visited:
12                return False
13            visited.add(crs)
14            for pre in preMap[crs]:
15                if not dfs(pre):
16                    return False
17            visited.remove(crs)
18            preMap[crs] = []
19            return True
20        for crs in range(numCourses):
21            if not dfs(crs):
22                return False
23        return True
24