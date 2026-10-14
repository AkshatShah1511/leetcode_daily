# LeetCode 153: Find Minimum in Rotated Sorted Array
# https://leetcode.com/problems/find-minimum-in-rotated-sorted-array/
# Added: 2026-10-14 (Asia/Calcutta)
# Selection: Fallback; today's official daily challenge could not be verified.
#
# Approach:
# Use binary search. Compare the middle value with the rightmost value. If the
# middle value is larger, the rotation point and minimum must be to its right.
# Otherwise, the middle value may itself be the minimum, so keep it and discard
# only the portion strictly to its right.
#
# Correctness:
# The minimum always remains inside the inclusive interval [left, right]. When
# nums[mid] > nums[right], mid lies before the rotation point, so the minimum
# is in [mid + 1, right]. Otherwise, the sorted portion from mid through right
# contains no value smaller than nums[mid], so the minimum is in [left, mid].
# Each update preserves the invariant and shrinks the interval. At termination,
# left == right, and that remaining element is therefore the array minimum.
#
# Time complexity: O(log n), where n is the length of nums.
# Space complexity: O(1).

from typing import List


class Solution:
    def findMin(self, nums: List[int]) -> int:
        left, right = 0, len(nums) - 1

        while left < right:
            middle = left + (right - left) // 2

            if nums[middle] > nums[right]:
                # The minimum lies strictly after middle.
                left = middle + 1
            else:
                # Middle may be the minimum, so keep it in the search range.
                right = middle

        return nums[left]
