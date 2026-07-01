class Solution:
    def longestPalindrome(self, s: str) -> str:
        max = ""
        for i in range(len(s)):
            sub = ""

            for j in range(i, len(s)):
                sub += s[j]
                if self.isPalindrome(sub) and len(sub) > len(max):
                    max = sub
        return max

    def isPalindrome(self, s):
        if s == s[::-1]:
            return True
        return False


