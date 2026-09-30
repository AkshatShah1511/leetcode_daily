# LeetCode 14: Longest Common Prefix
# https://leetcode.com/problems/longest-common-prefix/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Compare each column across all strings until the first disagreement.
# Complexity: O(total characters) time, O(number of strings) transient space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def longestCommonPrefix(self, strs: List[str]) -> str:
        if not strs: return ''
        length = 0
        for column in zip(*strs):
            if len(set(column)) != 1: break
            length += 1
        return strs[0][:length]
