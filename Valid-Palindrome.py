1class Solution:
2    def isPalindrome(self, s: str) -> bool:
3        '''        
4        s_non_alph_num = re.sub(r'[^a-zA-Z0-9]', '', s).lower()
5        if s_non_alph_num == s_non_alph_num[::-1]:
6            return True
7        return False'''
8
9        l, r = 0, len(s) - 1
10        while l<r:
11            while l<r and not s[l].isalnum():
12                l += 1
13            while l<r and not s[r].isalnum():
14                r -= 1
15            if s[l].lower() != s[r].lower():
16                return False
17            l = l + 1
18            r = r - 1
19        return True
20