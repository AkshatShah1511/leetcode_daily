# LeetCode 26: Remove Duplicates from Sorted Array
# https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Imported: 2026-09-30.
# Approach: Write each new sorted value into the next free prefix position.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def removeDuplicates(self, nums: List[int]) -> int:
        write = 0
        for value in nums:
            if write == 0 or value != nums[write-1]:
                nums[write] = value
                write += 1
        return write
