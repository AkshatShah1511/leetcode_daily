# LeetCode 128: Longest Consecutive Sequence
# https://leetcode.com/problems/longest-consecutive-sequence/
# Added: 2026-10-16 (Asia/Calcutta)
# Selection: Fallback; today's official daily challenge could not be verified.
#
# Approach:
# Put every value in a set. A value can start a consecutive sequence only when
# its predecessor is absent. From each such start, count upward while the next
# integer exists in the set, and keep the longest length found.
#
# Correctness:
# Every consecutive sequence has exactly one smallest value, whose predecessor
# is not in the set, so the algorithm starts counting each sequence exactly at
# that value. The inner loop then visits every successive member until the first
# missing integer, producing that sequence's exact length. Taking the maximum
# over all sequence starts therefore returns the longest consecutive length.
#
# Time complexity: O(n) expected time, where n is the length of nums.
# Space complexity: O(n) for the set of distinct values.

from typing import List


class Solution:
    def longestConsecutive(self, nums: List[int]) -> int:
        values = set(nums)
        longest = 0

        for value in values:
            # Only the smallest member of a sequence begins a scan.
            if value - 1 in values:
                continue

            current = value
            length = 1

            while current + 1 in values:
                current += 1
                length += 1

            longest = max(longest, length)

        return longest
