# LeetCode 198: House Robber
# https://leetcode.com/problems/house-robber/
# Added: 2026-10-03 (Asia/Calcutta)
# Selection: Fallback; today's official daily challenge could not be verified.
#
# Approach:
# For each house, either skip it and keep the best total for the preceding
# prefix, or take its money plus the best total ending before its neighbor.
# Keep only those two prefix totals instead of an entire DP array.
#
# Correctness:
# Before processing a house, one_back is the optimal total for all preceding
# houses, and two_back is the optimal total excluding the immediate neighbor.
# An optimal selection either skips the current house (one_back), or takes
# it and cannot take its neighbor (two_back + money). These cases cover every
# valid selection, so their maximum is the new optimal prefix total.
# Both empty-prefix totals start at zero. Updating the two values preserves
# the invariant, and after the last house one_back is the required optimum.
#
# Complexity: O(n) time and O(1) auxiliary space.

from typing import List


class Solution:
    def rob(self, nums: List[int]) -> int:
        two_back = 0
        one_back = 0

        for money in nums:
            # Compute before shifting so both choices use the old totals.
            best = max(one_back, two_back + money)
            two_back = one_back
            one_back = best

        return one_back
