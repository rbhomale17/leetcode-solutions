class Solution:
    def minCostClimbingStairs(self, cost: List[int]) -> int:
        dp = [None for _ in cost]
        # print(dp)
        return self.recursion(0, cost, dp)

    def recursion(self, index, cost, dp):
        # print(f'index: {index}, dp: {dp}')
        if index >= len(cost) - 1:
            return 0

        if dp[index] is not None:
            return dp[index]

        dp[index] = min(
            (cost[index] + self.recursion(index + 1, cost, dp)),
            (cost[index + 1] + self.recursion(index + 2, cost, dp)),
        )
        # print(dp, index)
        return dp[index]


