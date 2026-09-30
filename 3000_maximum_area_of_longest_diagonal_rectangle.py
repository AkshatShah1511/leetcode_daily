# LeetCode 3000: Maximum Area of Longest Diagonal Rectangle
# https://leetcode.com/problems/maximum-area-of-longest-diagonal-rectangle/
# Imported: 2026-09-30.
# Approach: Compare squared diagonal lengths, breaking ties by area.
# Complexity: O(n) time, O(1) auxiliary space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def areaOfMaxDiagonal(self, dimensions: List[List[int]]) -> int:
        return max((a*a+b*b,a*b) for a,b in dimensions)[1]
