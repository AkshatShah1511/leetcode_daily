# LeetCode 28: Find the Index of the First Occurrence in a String
# https://leetcode.com/problems/find-the-index-of-the-first-occurrence-in-a-string/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: KMP reuses the longest matching prefix after each mismatch.
# Complexity: O(n+m) time, O(m) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def strStr(self, haystack: str, needle: str) -> int:
        if not needle: return 0
        prefix = [0]*len(needle)
        j = 0
        for i in range(1,len(needle)):
            while j and needle[i] != needle[j]: j = prefix[j-1]
            if needle[i] == needle[j]: j += 1
            prefix[i] = j
        j = 0
        for i,ch in enumerate(haystack):
            while j and ch != needle[j]: j = prefix[j-1]
            if ch == needle[j]: j += 1
            if j == len(needle): return i-j+1
        return -1
