# LeetCode 300: Longest Increasing Subsequence
# https://leetcode.com/problems/longest-increasing-subsequence/
# Added: 2026-10-08 (Asia/Calcutta)
# Selection: Fallback; today's official daily challenge could not be verified.
#
# Approach:
# Maintain tails, where tails[i] is the smallest possible final value of any
# strictly increasing subsequence of length i + 1 seen so far. For each number,
# binary-search the first tail greater than or equal to it. Replace that tail,
# or append the number if it is larger than every existing tail.
#
# Correctness:
# Replacing the first tail >= number preserves the represented subsequence
# length while making its ending value no larger, so it cannot reduce future
# extension opportunities. Appending happens exactly when number is larger
# than every tail, which extends the longest known increasing subsequence.
# Because equal values replace rather than append, only strict increases grow
# the length. Therefore, after all values are processed, len(tails) equals the
# length of the longest strictly increasing subsequence.
#
# Complexity: O(n log n) time and O(n) auxiliary space.

from bisect import bisect_left
from typing import List


class Solution:
    def lengthOfLIS(self, nums: List[int]) -> int:
        tails: List[int] = []

        for number in nums:
            position = bisect_left(tails, number)

            if position == len(tails):
                tails.append(number)
            else:
                tails[position] = number

        return len(tails)
