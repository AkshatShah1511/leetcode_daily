# LeetCode 56: Merge Intervals
# https://leetcode.com/problems/merge-intervals/
# Added: 2026-10-17 (Asia/Calcutta)
# Selection: Fallback; today's official daily challenge could not be verified.
#
# Approach:
# Sort intervals by their starting point. Scan them from left to right, adding
# a new result interval when there is a gap and extending the last result when
# the current interval overlaps it.
#
# Correctness:
# After processing each interval, the result contains exactly the merged union
# of all processed intervals, in sorted non-overlapping order. If the current
# start is after the last merged end, it cannot overlap any earlier interval,
# so appending it preserves the invariant. Otherwise it overlaps the last
# merged interval, and extending that interval's end to the larger endpoint
# preserves exactly their union. Thus the invariant holds through the complete
# scan, and the returned intervals are the required merged coverage.
#
# Time complexity: O(n log n) for sorting n intervals.
# Space complexity: O(n) for the sorted list and output.

from typing import List


class Solution:
    def merge(self, intervals: List[List[int]]) -> List[List[int]]:
        if not intervals:
            return []

        ordered = sorted(intervals, key=lambda interval: interval[0])
        merged = [ordered[0].copy()]

        for start, end in ordered[1:]:
            if start > merged[-1][1]:
                # A positive gap begins a new non-overlapping interval.
                merged.append([start, end])
            else:
                # Touching endpoints count as overlap.
                merged[-1][1] = max(merged[-1][1], end)

        return merged
