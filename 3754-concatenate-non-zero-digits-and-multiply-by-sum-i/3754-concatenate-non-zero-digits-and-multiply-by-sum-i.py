class Solution:
    def sumAndMultiply(self, number: int) -> int:
        x_num = 0
        x_sum = 0

        for num in str(number):
            n = int(num)
            if n != 0:    
                x_num = (x_num * 10) + n
                x_sum += n        
        
        # print(x_num, x_sum)
        return x_num * x_sum



# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna