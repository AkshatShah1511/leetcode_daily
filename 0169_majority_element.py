# LeetCode 169: Majority Element
# https://leetcode.com/problems/majority-element/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Boyer-Moore cancels unlike pairs; the guaranteed majority survives.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        count,candidate = 0,None
        for x in nums:
            if count == 0: candidate = x
            count += 1 if x == candidate else -1
        return candidate
