import math

class Solution:
    def isPalindrome(self, x: int) -> bool:
        n = 0
        a_x = x

        while(x > 0):

            last = x % 10
            n = n * 10 + last

            x = math.floor(x / 10)
        

        return a_x == n

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna