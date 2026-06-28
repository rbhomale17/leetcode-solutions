class Solution:
    def myAtoi(self, s: str) -> int:
        s = s.lstrip(' ')
        if not s or (not s[0].isdigit() and s[0] not in ['-', '+']):
            return 0
        MIN_INT = -2 ** 31
        MAX_INT = 2 ** 31 -1
        print(s)
        sym = 1
        res = 0
        # digit_found = False
        for i, ch in enumerate(s):
            is_curr_digit = ch.isdigit()
            print(i, ch, is_curr_digit, res)
            if i == 0 and not is_curr_digit:
                if ch == '-':
                    sym = -1
                else:
                    sym = 1
            elif is_curr_digit:
                res = res * 10 + int(ch)
            else:
                break
        num = res * sym

        if num < MIN_INT:
            return MIN_INT
        elif num > MAX_INT:
            return MAX_INT
        else:
            return num

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna