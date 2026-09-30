# LeetCode 67: Add Binary
# https://leetcode.com/problems/add-binary/
# Imported: 2026-09-30.
# Approach: Add bits from right to left with a binary carry.
# Complexity: O(m+n) time and output space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def addBinary(self, a: str, b: str) -> str:
        i,j,carry = len(a)-1,len(b)-1,0
        out = []
        while i >= 0 or j >= 0 or carry:
            if i >= 0: carry += int(a[i]); i -= 1
            if j >= 0: carry += int(b[j]); j -= 1
            out.append(str(carry%2)); carry //= 2
        return ''.join(reversed(out))
