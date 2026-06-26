import math

class Solution:
    def pivotInteger(self, n: int) -> int:
        pivot = math.sqrt(n * (n + 1) / 2)
        if pivot.is_integer():
            return int(pivot)
        else:
            return -1


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna