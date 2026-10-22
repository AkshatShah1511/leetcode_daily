# LeetCode 78: Subsets
# https://leetcode.com/problems/subsets/
# Added: 2026-10-22 (Asia/Calcutta)
# Selection: Fallback; the official daily challenge could not be verified.
#
# Approach:
# Start with the empty subset. For every number, copy each subset that already
# exists, append the number to that copy, and add the new subset to the answer.
# This represents the two choices for every element: exclude it or include it.
#
# Correctness:
# After processing the first k numbers, the result contains every subset of
# those k numbers exactly once. For the next number, the old subsets cover all
# subsets that exclude it, while their copied-and-extended versions cover all
# subsets that include it. These two groups are disjoint, so the invariant is
# preserved. After all numbers are processed, every subset appears exactly once.
#
# Time complexity: O(n * 2^n), including construction of all returned subsets.
# Space complexity: O(n * 2^n) for the returned subsets; O(1) auxiliary space.

from typing import List


class Solution:
    def subsets(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = [[]]

        for number in nums:
            # Only extend subsets that existed before processing this number.
            existing_count = len(result)
            for index in range(existing_count):
                result.append(result[index] + [number])

        return result
