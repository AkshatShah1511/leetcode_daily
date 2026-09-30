# LeetCode 1009: Complement of Base 10 Integer
# https://leetcode.com/problems/complement-of-base-10-integer/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: XOR with a mask containing one bit for each significant bit; zero needs one bit.
# Complexity: O(1) fixed-width time and space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def bitwiseComplement(self, n: int) -> int:
        return n ^ ((1<<max(1,n.bit_length()))-1)
