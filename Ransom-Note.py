1class Solution:
2    def canConstruct(self, ransomNote: str, magazine: str) -> bool:
3        ransomNoteHash = {}
4        
5        for char in ransomNote:
6            ransomNoteHash[char] = ransomNoteHash.get(char, 0) + 1
7        
8        for char in magazine:
9            if char in ransomNoteHash:
10                ransomNoteHash[char] -= 1
11        
12        for count in ransomNoteHash.values():
13            if count > 0:
14                return False
15        return True