# LeetCode 231: Power of Two
# https://leetcode.com/problems/power-of-two/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: A positive power of two contains exactly one set bit.
# Complexity: O(1) time and space for fixed-width input.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def isPowerOfTwo(self, n: int) -> bool:
        return n > 0 and (n & (n-1)) == 0
