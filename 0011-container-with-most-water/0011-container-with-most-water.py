class Solution:
    def maxArea(self, height: List[int]) -> int:
        
        max_w = 0

        i = 0
        j = len(height) - 1

        while i <= j:
            area = min(height[i], height[j]) * (j-i)
            if height[i] <= height[j]:
                i += 1
            else:
                j -= 1

            max_w = max(area, max_w)

        return max_w


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna