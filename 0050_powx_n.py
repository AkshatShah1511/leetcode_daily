# LeetCode 50: Pow(x, n)
# https://leetcode.com/problems/powx-n/
# Imported: 2026-09-30.
# Approach: Binary exponentiation squares the base and consumes one exponent bit at a time.
# Complexity: O(log abs(n)) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def myPow(self, x: float, n: int) -> float:
        if n < 0: x, n = 1/x, -n
        answer = 1.0
        while n:
            if n & 1: answer *= x
            x *= x
            n >>= 1
        return answer
