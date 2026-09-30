# LeetCode 43: Multiply Strings
# https://leetcode.com/problems/multiply-strings/
# Imported: 2026-09-30.
# Approach: Multiply every digit pair into its positional slot, then propagate carries.
# Complexity: O(m*n) time, O(m+n) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def multiply(self, num1: str, num2: str) -> str:
        digits = [0]*(len(num1)+len(num2))
        for i in range(len(num1)-1,-1,-1):
            for j in range(len(num2)-1,-1,-1):
                digits[i+j+1] += (ord(num1[i])-48)*(ord(num2[j])-48)
        for i in range(len(digits)-1,0,-1):
            digits[i-1] += digits[i]//10
            digits[i] %= 10
        return ''.join(map(str,digits)).lstrip('0') or '0'
