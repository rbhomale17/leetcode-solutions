class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        target = 0
        nums.sort()
        res = []

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue

            start = i + 1
            end = len(nums) - 1

            while start < end:
                total = nums[i] + nums[start] + nums[end]
                # print(total, nums[i], nums[start], nums[end])

                if total == target:
                    res.append([nums[i], nums[start], nums[end]])
                    start += 1
                    end -= 1

                    while start < end and nums[start] == nums[start - 1]: start += 1
                    while start < end and nums[end] == nums[end + 1]: end -= 1
                elif total < target:
                    start += 1
                else:
                    end -= 1
        return res


# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna