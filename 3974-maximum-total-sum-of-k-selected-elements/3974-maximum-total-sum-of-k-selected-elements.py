class Solution:
    def maxSum(self, nums: list[int], k: int, mul: int) -> int:
        nums.sort(reverse=True)
        # print(nums)
        ns = nums[:k]

        total = 0

        for dig in ns:
            if mul >= 1:
                total = total + (dig * mul)
                mul -= 1
            else:
                total += dig

        # print(total)
        # print(nums[:k])

        return total


