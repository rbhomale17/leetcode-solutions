class Solution:
    # normal loop max1 max2 O(N)
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        maxi_1 = maxi_2 = 0

        for num in nums:
            if num > maxi_1:
                maxi_2 = maxi_1
                maxi_1 = num
        
        return (maxi_1 - 1) * (maxi_2 - 1)


    # Sorting method O( NlogN)
    def maxProduct(self, nums: List[int]) -> int:
        n = len(nums)
        nums.sort()
        return (nums[n - 1] - 1) * (nums[n - 2] - 1)

    

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna