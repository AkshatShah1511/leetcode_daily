# LeetCode 27: Remove Element
# https://leetcode.com/problems/remove-element/
# Imported: 2026-09-30.
# Approach: Compact values unequal to val into a valid prefix.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def removeElement(self, nums: List[int], val: int) -> int:
        write = 0
        for x in nums:
            if x != val:
                nums[write] = x
                write += 1
        return write
