from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        dp = {0: 0}
        for i in range(1, amount + 1):
            dp.setdefault(i, float("inf"))
            for coin in coins:
                if 0 <= i - coin and dp[i - coin] != -1:
                    dp[i] = min(dp[i - coin] + 1, dp[i])

        if dp[amount] == float("inf"):
            return -1
        return dp[amount]
