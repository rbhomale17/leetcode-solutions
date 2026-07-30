class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s > n * 9:
            return -1
        elif s == 0:
            return 0
        
        digits = 0
        while n > 0:
            digits = digits * 10 + 9
            n = n - 1

        while digits > 0 :
            if sum(int(x) for x in str(digits)) == s:
                return digits

            digits = digits - 1

        return -1       




