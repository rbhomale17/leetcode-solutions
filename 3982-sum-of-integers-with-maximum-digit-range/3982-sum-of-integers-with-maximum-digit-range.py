class Solution:
    def maxDigitRange(self, nums: list[int]) -> int:
        maxi = 0
        maxi_idx = []
        for i in range(len(nums)):
            num = str(nums[i])
            # print(num, type(num))
            # print(min(num), max(num))
            diff = abs(int(min(num)) - int(max(num)))
            # print(f"diff: {diff}, maxi: {maxi}, maxi_idx: {maxi_idx}, maxi > diff: {maxi > diff}, maxi == diff: {maxi == diff}")
            if diff > maxi:
                maxi_idx = [i]
                maxi = diff
            elif maxi == diff:
                maxi_idx.append(i)
                maxi = diff
        # print(maxi, maxi_idx)

        res = 0
        for i in maxi_idx:
            res += nums[i]
        
        return res

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna