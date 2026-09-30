# LeetCode 3823: Reverse Letters Then Special Characters in a String
# https://leetcode.com/problems/reverse-letters-then-special-characters-in-a-string/
# Imported: 2026-09-30.
# Approach: Collect the two character categories separately and pop each in reverse order.
# Complexity: O(n) time and space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def reverseByType(self, s: str) -> str:
        letters=[ch for ch in s if 'a'<=ch<='z']
        special=[ch for ch in s if not 'a'<=ch<='z']
        return ''.join(letters.pop() if 'a'<=ch<='z' else special.pop() for ch in s)
