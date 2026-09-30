# LeetCode 121: Best Time to Buy and Sell Stock
# https://leetcode.com/problems/best-time-to-buy-and-sell-stock/
# Imported: 2026-09-30.
# Approach: Track the cheapest earlier purchase and the best profit from selling today.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def maxProfit(self, prices: List[int]) -> int:
        low,profit = float('inf'),0
        for price in prices:
            low = min(low,price); profit = max(profit,price-low)
        return profit
