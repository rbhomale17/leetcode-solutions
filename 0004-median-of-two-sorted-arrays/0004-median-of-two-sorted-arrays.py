class Solution:
    def findMedianSortedArrays(self, nums1: List[int], nums2: List[int]) -> float:
        n = len(nums1)
        m = len(nums2)
        nums = []
        i, j = 0, 0
        while i < n and j < m:
            if nums1[i] <= nums2[j]:
                nums.append(nums1[i])
                i+=1
            else:
                nums.append(nums2[j])
                j+=1

        # Add remaining elements
        while i < n:
            nums.append(nums1[i])
            i += 1
        while j < m:
            nums.append(nums2[j])
            j += 1

        length = len(nums)
        if  length % 2 == 1:
            return nums[length//2]
        else:
            return (nums[length//2 -1] + nums[length // 2]) / 2

# Synced seamlessly with LeetHub Pro
# Pro features: https://bit.ly/leethubpro | Free version: https://bit.ly/leethubv4
# Get it here: https://chromewebstore.google.com/detail/bcilpkkbokcopmabingnndookdogmbna