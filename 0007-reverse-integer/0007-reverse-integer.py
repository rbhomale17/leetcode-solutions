class Solution:
    def reverse(self, x: int) -> int:
        is_negative = True if x < 0 else False
        x = x * -1 if is_negative else x

        rev = 0

        while x > 0:
            last = x % 10
            rev = rev * 10 + last
            x //= 10
        
        rev = rev * -1 if is_negative else rev
        
        if rev > 2 ** 31 - 1 or rev < -2 ** 31:
            return 0
        return rev

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna