# LeetCode 322: Coin Change
# https://leetcode.com/problems/coin-change/
# Added: 2026-10-04 (Asia/Calcutta)
# Selection: Fallback; today's official daily challenge could not be verified.
#
# Approach:
# Use bottom-up dynamic programming. For every total from 1 through amount,
# try each coin that does not exceed that total. If dp[total - coin] is the
# fewest coins needed for the remaining value, adding this coin creates a
# candidate solution for total. Store the smallest candidate.
#
# Correctness:
# Let dp[x] be the minimum number of coins needed to form x. The base case
# dp[0] = 0 is correct because no coins are required. For each positive x,
# every valid combination ends with some coin c and has a preceding
# combination totaling x - c. When x is processed, dp[x - c] is already
# optimal. Taking the minimum of dp[x - c] + 1 over all usable coins
# therefore considers every possible final coin and yields the optimum.
# If no candidate is reachable, x cannot be formed and the answer is -1.
#
# Complexity: O(amount * len(coins)) time and O(amount) auxiliary space.

from typing import List


class Solution:
    def coinChange(self, coins: List[int], amount: int) -> int:
        unreachable = amount + 1
        dp = [unreachable] * (amount + 1)
        dp[0] = 0

        for total in range(1, amount + 1):
            for coin in coins:
                if coin <= total:
                    dp[total] = min(dp[total], dp[total - coin] + 1)

        return -1 if dp[amount] == unreachable else dp[amount]
