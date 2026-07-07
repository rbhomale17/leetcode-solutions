class Solution:
    def sumAndMultiply(self, n: int) -> int:
        x = [int(num) for num in str(n) if int(num) > 0]
        # print(x, type(x))

        x_num = 0
        x_sum = 0
        i = 0
        while i < len(x):
            digit = x[i]
            x_num = (x_num * 10) + digit
            x_sum += digit
        
            i += 1
        
        # print(x_num, x_sum)
        return x_num * x_sum



