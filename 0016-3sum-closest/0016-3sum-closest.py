class Solution:
    def threeSumClosest(self, nums: List[int], target: int) -> int:
        nums.sort()
        closest = nums[0] + nums[1] + nums[2]

        for i in range(len(nums)):
            if i > 0 and nums[i] == nums[i - 1]: continue # Skip duplicates
            start = i + 1
            end = len(nums) - 1
            while start < end:
                total = nums[i] + nums[start] + nums[end]
                if abs(target - total) < abs(target - closest):
                    closest = total
                if total < target:
                    start += 1
                elif total > target:
                    end -= 1
                else:
                    return total

        return closest

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna