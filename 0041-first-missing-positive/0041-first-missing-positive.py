class Solution:
    def firstMissingPositive(self, nums: List[int]) -> int:
            n = len(nums)
            print(nums)
            for i in range(n):
                while 1 <= nums[i] <= n and nums[nums[i] - 1] != nums[i]:
                    nums[nums[i] - 1], nums[i] = nums[i], nums[nums[i] - 1]
            
            # print(nums)

            for i in range(n):
                if nums[i] != i + 1:
                    return i + 1

            return n + 1

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna