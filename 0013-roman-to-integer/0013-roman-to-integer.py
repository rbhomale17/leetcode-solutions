class Solution:
    def romanToInt(self, s: str) -> int:
        roman = {
            "I":1,
            "V":5,
            "X":10,
            "L":50,
            "C":100,
            "D":500,
            "M":1000
        }

        total = 0
        i = 0
        while i < len(s):
            curr = roman[s[i]]
            next_val = roman[s[i + 1]] if i + 1 < len(s) else 0

            if next_val and curr < next_val :
                total += next_val - curr
                i+=2
            else:
                total += curr
                i+=1
        print(total)
        return total

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna