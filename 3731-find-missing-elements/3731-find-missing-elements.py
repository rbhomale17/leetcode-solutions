class Solution:
    def findMissingElements(self, nums: List[int]) -> List[int]:
        obj = set(nums)
        # print(obj)

        mini = min(nums)
        maxi = max(nums)

        # print(mini, maxi)

        result = []

        for num in range(mini + 1, maxi):
            if num not in obj:
                result.append(num)

        return result

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna