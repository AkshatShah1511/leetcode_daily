# LeetCode 35: Search Insert Position
# https://leetcode.com/problems/search-insert-position/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Lower bound is the first position whose value is not smaller than target.
# Complexity: O(log n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

from bisect import bisect_left
class Solution:
    def searchInsert(self, nums: List[int], target: int) -> int:
        return bisect_left(nums,target)
