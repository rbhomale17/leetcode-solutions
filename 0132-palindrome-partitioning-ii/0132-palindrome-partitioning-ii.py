class Solution:
    def minCut(self, s: str) -> int:
        n = len(s)
        if n <= 1:
            return 0
        
        # Step 1: Precompute palindrome table
        is_palindrome = [[False]*n for _ in range(n)]
        for end in range(n):
            for start in range(end + 1):
                if s[start] == s[end] and (end - start <= 2 or is_palindrome[start+1][end-1]):
                    is_palindrome[start][end] = True
        
        # Step 2: DP for minimum cuts
        dp = [0]*n
        for i in range(n):
            if is_palindrome[0][i]:
                dp[i] = 0
            else:
                dp[i] = float('inf')
                for j in range(i):
                    if is_palindrome[j+1][i]:
                        dp[i] = min(dp[i], dp[j] + 1)
        
        return dp[-1]

        

