class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False

        a = [0] * 26
        b = [0] * 26

        for ch in range(len(s)):
            a[ord(s[ch]) - ord("a")] += 1
            b[ord(t[ch]) - ord("a")] += 1
        
        return a == b

        