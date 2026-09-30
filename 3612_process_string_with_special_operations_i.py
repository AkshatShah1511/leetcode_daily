# LeetCode 3612: Process String with Special Operations I
# https://leetcode.com/problems/process-string-with-special-operations-i/
# Imported: 2026-09-30.
# Approach: Simulate each operation on a character list in the stated order.
# Complexity: O(n*M) time, O(M) space; M is maximum intermediate output length.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def processStr(self, s: str) -> str:
        result=[]
        for ch in s:
            if ch=='*':
                if result: result.pop()
            elif ch=='#': result.extend(result[:])
            elif ch=='%': result.reverse()
            else: result.append(ch)
        return ''.join(result)
