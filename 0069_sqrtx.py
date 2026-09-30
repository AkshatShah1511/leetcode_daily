# LeetCode 69: Sqrt(x)
# https://leetcode.com/problems/sqrtx/
# Imported: 2026-09-30.
# Approach: Binary-search the largest integer whose square is at most x.
# Complexity: O(log(x+1)) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def mySqrt(self, x: int) -> int:
        lo,hi = 0,x
        while lo <= hi:
            mid = (lo+hi)//2
            if mid*mid <= x: lo = mid+1
            else: hi = mid-1
        return hi
