# LeetCode 77: Combinations
# https://leetcode.com/problems/combinations/
# Added: 2026-10-29 (Asia/Calcutta)
# Selection: Fallback; the official daily challenge could not be verified.
#
# Approach:
# Use backtracking to build each combination in strictly increasing order.
# At every step, try each possible next number, but stop early when too few
# numbers remain to complete a combination of length k.
#
# Correctness:
# Every generated path is strictly increasing and has exactly k values, so it
# is a valid combination. Conversely, any k-combination can be written in
# increasing order; the search follows that exact sequence of choices and
# therefore generates it. Strict ordering also prevents duplicates, so every
# valid combination appears exactly once.
#
# Time complexity: O(k * C(n, k)), including construction of the output.
# Space complexity: O(k) auxiliary space for the recursion path, excluding
# the returned combinations.

from typing import List


class Solution:
    def combine(self, n: int, k: int) -> List[List[int]]:
        combinations: List[List[int]] = []
        current: List[int] = []

        def backtrack(start: int) -> None:
            if len(current) == k:
                combinations.append(current.copy())
                return

            # If `needed` values are still required, the next value cannot be
            # greater than n - needed + 1, or completion would be impossible.
            needed = k - len(current)
            last_start = n - needed + 1

            for value in range(start, last_start + 1):
                current.append(value)
                backtrack(value + 1)
                current.pop()

        backtrack(1)
        return combinations
