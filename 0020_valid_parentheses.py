# LeetCode 20: Valid Parentheses
# https://leetcode.com/problems/valid-parentheses/
# Imported: 2026-09-30.
# Approach: A stack stores unmatched opening brackets; each closer must match its top.
# Complexity: O(n) time, O(n) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def isValid(self, s: str) -> bool:
        stack = []
        pairs = {')':'(', ']':'[', '}':'{'}
        for ch in s:
            if ch in pairs:
                if not stack or stack.pop() != pairs[ch]: return False
            else: stack.append(ch)
        return not stack
