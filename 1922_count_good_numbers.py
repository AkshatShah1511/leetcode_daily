# LeetCode 1922: Count Good Numbers
# https://leetcode.com/problems/count-good-numbers/
# Imported: 2026-09-30.
# Approach: Even positions have five choices, odd positions four; multiply modular powers.
# Complexity: O(log n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def countGoodNumbers(self, n: int) -> int:
        mod=10**9+7
        return pow(5,(n+1)//2,mod)*pow(4,n//2,mod)%mod
