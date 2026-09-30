# LeetCode 13: Roman to Integer
# https://leetcode.com/problems/roman-to-integer/
# Imported: 2026-09-30.
# Approach: Subtract a symbol only when the next symbol is larger; otherwise add it.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def romanToInt(self, s: str) -> int:
        values = dict(I=1, V=5, X=10, L=50, C=100, D=500, M=1000)
        return sum(-values[c] if i+1 < len(s) and values[c] < values[s[i+1]] else values[c]
                   for i,c in enumerate(s))
