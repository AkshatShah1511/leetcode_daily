# LeetCode 70: Climbing Stairs
# https://leetcode.com/problems/climbing-stairs/
# Added: 2026-10-01 (Asia/Calcutta)
# Selection: Fallback; today's official daily challenge could not be verified.
#
# Approach:
# A climb to step i ends with either a one-step move from i-1 or a
# two-step move from i-2. These disjoint possibilities give
# ways(i) = ways(i-1) + ways(i-2).
# Keep only the previous two counts instead of a full DP array.
#
# Correctness:
# There is one way to climb zero steps (take no moves), and one way
# to climb one step. Before processing step i, the two stored values
# equal ways(i-2) and ways(i-1). Their sum therefore counts every
# climb to i exactly once according to its final move. Updating the
# pair preserves this invariant, so the returned value is ways(n).
#
# Complexity: O(n) time and O(1) auxiliary space for 1 <= n <= 45.

class Solution:
    def climbStairs(self, n: int) -> int:
        two_back = 1  # ways(0)
        one_back = 1  # ways(1)

        for step in range(2, n + 1):
            # Simultaneous assignment uses both counts from the prior step.
            two_back, one_back = one_back, two_back + one_back

        return one_back
