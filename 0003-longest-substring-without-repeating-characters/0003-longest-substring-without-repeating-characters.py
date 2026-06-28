# class Solution:
#     def lengthOfLongestSubstring(self, s: str) -> int:
#         char_index = {}
#         max_len = 0
#         i = 0
        
#         for j in range(len(s)):
#             if s[j] in char_index and char_index[s[j]] >= i:
#                 i = char_index[s[j]] + 1
            
#             char_index[s[j]] = j
#             max_len = max(max_len, j - i + 1)
        
#         return max_len

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        n = len(s)
        visit = set()
        
        i = 0
        j = 0
        max_len = 0
        
        while j < n:
            if s[j] not in visit:
                visit.add(s[j])
                max_len = max(max_len, j - i + 1)
                j += 1
            else:
                visit.remove(s[i])
                i += 1
        
        return max_len

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna