# LeetCode 75: Sort Colors
# https://leetcode.com/problems/sort-colors/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Dutch flag partitions the array into zeros, ones, unknowns, and twos.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def sortColors(self, nums: List[int]) -> None:
        low = scan = 0
        high = len(nums)-1
        while scan <= high:
            if nums[scan] == 0:
                nums[low],nums[scan] = nums[scan],nums[low]
                low += 1; scan += 1
            elif nums[scan] == 2:
                nums[scan],nums[high] = nums[high],nums[scan]
                high -= 1  # The swapped-in value remains unclassified.
            else: scan += 1
