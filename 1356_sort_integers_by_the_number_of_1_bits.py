# LeetCode 1356: Sort Integers by The Number of 1 Bits
# https://leetcode.com/problems/sort-integers-by-the-number-of-1-bits/
# Imported: 2026-09-30.
# Approach: Sort by population count first and integer value second.
# Complexity: O(n log n) time, O(n) space for fixed-width integers.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def sortByBits(self, arr: List[int]) -> List[int]:
        return sorted(arr,key=lambda x:(x.bit_count(),x))
