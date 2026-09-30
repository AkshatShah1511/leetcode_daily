# LeetCode 33: Search in Rotated Sorted Array
# https://leetcode.com/problems/search-in-rotated-sorted-array/
# Imported: 2026-09-30.
# Approach: At least one half is sorted; test whether the target lies inside that half.
# Complexity: O(log n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo, hi = 0, len(nums)-1
        while lo <= hi:
            mid = (lo+hi)//2
            if nums[mid] == target: return mid
            if nums[lo] <= nums[mid]:
                if nums[lo] <= target < nums[mid]: hi = mid-1
                else: lo = mid+1
            else:
                if nums[mid] < target <= nums[hi]: lo = mid+1
                else: hi = mid-1
        return -1
