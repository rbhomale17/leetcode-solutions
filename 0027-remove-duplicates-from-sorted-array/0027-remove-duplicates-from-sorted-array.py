class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        i = 1

        while i < len(nums):
            if nums[i] == nums[i - 1]:
                nums.pop(i)
                continue
            i += 1
        print(nums)

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna