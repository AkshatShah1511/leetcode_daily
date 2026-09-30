# LeetCode 58: Length of Last Word
# https://leetcode.com/problems/length-of-last-word/
# Imported: 2026-09-30.
# Approach: Scan backward past trailing spaces, then count the final word.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def lengthOfLastWord(self, s: str) -> int:
        i = len(s)-1
        while i >= 0 and s[i] == ' ': i -= 1
        end = i
        while i >= 0 and s[i] != ' ': i -= 1
        return end-i
