class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        s = s.strip()
        word_count = 0
        for i in range(len(s) - 1, -1, -1):
            if s[i] == " ":
                return word_count
            else:
                word_count += 1
        return word_count