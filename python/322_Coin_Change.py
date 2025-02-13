class Solution:
    def coinChange(self, coins: list[int], amount: int) -> int:
        def helper(remain, dp: dict):
            if remain < 0:
                return float('inf')

            if remain == 0:
                return 0

            if remain in dp:
                return dp[remain]

            dp[remain] = min(1 + helper(remain - coin, dp) for coin in coins)

            return dp[remain]

        res = helper(amount, {})
        return -1 if res == float('inf') else res


print(Solution().coinChange([1, 2, 5], 11))  # 3
