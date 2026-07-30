class Solution:
    def largestInteger(self, n: int, s: int) -> int:
        if s > n * 9:
            return -1
        elif s == 0:
            return 0
        
        num_string = ''

        for x in range(n):
            curr_digit = min(s, 9)
            num_string += str(curr_digit)
            s -= curr_digit

        # print(s, num_string) 
        if s != 0:
            return -1
        
        return int(num_string)

"""
Dry run N = 3, S = 15

if 15 > 3 * 9 False 
if 15 == 0 False

num_string = ""

loop start till N ie. 3 times

Iter 1:
s = 15
num_string = ""
curr_digit = min(s=15, 9) = 9
num_string = num_string + curr_digit = "" + 9 = "9"
s = s - curr_digit = 15 - 9 = 6

Iter 2:
s = 6
num_string = "9"
curr_digit = MIN(s=6, 9) = 6
num_string = num_string + curr_digit = "9" + "6" = "96"
s = s - curr_digit = 6 - 6 = 0

Iter 3:
s = 0
num_string = "96"
curr_digit = MIN(s=0, 9) = 0
num_string = num_string + curr_digit = "96" + "0" = "960"
s = s - curr_digit = 0 - 0 = 0

loop compleated 
num_string = "960"
s = 0

if s != 0: return -1
else return int(num_string)
"""


