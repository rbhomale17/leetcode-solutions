class Solution:
    def checkGoodInteger(self, n: int) -> bool:
        digitSum = 0
        squareSum = 0

        while n > 0:
            digit = n % 10
            digitSum += digit
            squareSum += digit ** 2
            print(digitSum, squareSum)
            n = n // 10

        return (squareSum - digitSum) >= 50

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna