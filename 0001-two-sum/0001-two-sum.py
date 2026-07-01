class Solution:
    # def twoSum(self, nums: List[int], target: int) -> List[int]:
    #     seen = {}

    #     for idx, num in enumerate(nums):
    #         remaining = target - num

    #         if remaining in seen:
    #             return [seen[remaining], idx]
            
    #         seen[num] = idx

    def twoSum(self, nums: List[int], target: int) -> List[int]:
        n = len(nums)
        for i in range(n - 1):
            for j in range(i + 1, n):
                if nums[i] + nums[j] == target:
                    return [i, j]
        return []  # No solution found
        


# class Solution:
#     def twoSum(self, nums: List[int], target: int) -> List[int]:
#         tuple_nums = [(num, idx) for idx, num in enumerate(nums)]

#         print(tuple_nums)

#         sorted_nums = sorted(tuple_nums)
#         print(sorted_nums)

#         i = 0
#         j = len(nums) - 1

#         while i < j:
#             sum = sorted_nums[i][0] + sorted_nums[j][0]
#             if sum == target:
#                 return [sorted_nums[i][1], sorted_nums[j][1]]
#             elif sum > target:
#                 j -= 1
#             else:
#                 i += 1

