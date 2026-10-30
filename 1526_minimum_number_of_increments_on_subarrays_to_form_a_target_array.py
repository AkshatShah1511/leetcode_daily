# LeetCode 1526: Minimum Number of Increments on Subarrays to Form a Target Array
# https://leetcode.com/problems/minimum-number-of-increments-on-subarrays-to-form-a-target-array/
# Added: 2026-10-30 (Asia/Calcutta)
# Selection: Fallback; the official daily challenge could not be verified.
#
# Approach:
# View target[i] as the height required at index i. The first position starts
# target[0] layers. For every later position, only a positive rise above the
# previous height forces new subarray operations; a flat or falling height can
# reuse operations that already started to the left. Add every positive rise.
#
# Correctness:
# At index 0, exactly target[0] operations must start. For each i > 0, if
# target[i] exceeds target[i - 1], at least their difference in new operations
# must start at i because earlier operations can cover at most target[i - 1]
# layers there. Starting exactly that many operations and ending active ones
# whenever the height falls constructs the complete target. Thus the computed
# lower bound is achievable and is the minimum number of operations.
#
# Time complexity: O(n), where n is the length of target.
# Space complexity: O(1) auxiliary space.

from typing import List


class Solution:
    def minNumberOperations(self, target: List[int]) -> int:
        operations = target[0]

        for previous, current in zip(target, target[1:]):
            if current > previous:
                operations += current - previous

        return operations
