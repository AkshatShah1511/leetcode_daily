# LeetCode 66: Plus One
# https://leetcode.com/problems/plus-one/
# Imported: 2026-09-30.
# Approach: Propagate a carry backward through consecutive nines.
# Complexity: O(n) time, O(1) auxiliary space; O(n) if a new leading digit is needed.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def plusOne(self, digits: List[int]) -> List[int]:
        for i in range(len(digits)-1,-1,-1):
            if digits[i] < 9:
                digits[i] += 1
                return digits
            digits[i] = 0
        return [1]+digits
