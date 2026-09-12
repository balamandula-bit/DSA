class Solution:
    def isPalindrome(self, s: str) -> bool:
        s = s.lower()
        n = ""
        for ch in s:
            if ch.isalnum():
                n = n + ch
        

        if not n:
            return True
        
        return n == n[::-1]


        
        