# LeetCode 5: Longest Palindromic Substring
# https://leetcode.com/problems/longest-palindromic-substring/
# Imported: 2026-09-30.
# Approach: Expand around every odd and even center; every palindrome has such a center.
# Complexity: O(n^2) time, O(1) auxiliary space excluding output.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def longestPalindrome(self, s: str) -> str:
        start = length = 0
        for center in range(len(s)):
            for left, right in ((center, center), (center, center + 1)):
                while left >= 0 and right < len(s) and s[left] == s[right]:
                    if right - left + 1 > length:
                        start, length = left, right - left + 1
                    left -= 1
                    right += 1
        return s[start:start + length]
