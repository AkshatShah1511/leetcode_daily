# LeetCode 34: Find First and Last Position of Element in Sorted Array
# https://leetcode.com/problems/find-first-and-last-position-of-element-in-sorted-array/
# Imported: 2026-09-30.
# Approach: Binary-search the lower and upper insertion boundaries of the target.
# Complexity: O(log n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

from bisect import bisect_left, bisect_right
class Solution:
    def searchRange(self, nums: List[int], target: int) -> List[int]:
        left = bisect_left(nums,target)
        if left == len(nums) or nums[left] != target: return [-1,-1]
        return [left,bisect_right(nums,target)-1]
