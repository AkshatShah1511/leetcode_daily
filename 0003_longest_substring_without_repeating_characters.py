# LeetCode 3: Longest Substring Without Repeating Characters
# https://leetcode.com/problems/longest-substring-without-repeating-characters/
# Imported: 2026-09-30.
# Approach: Keep a duplicate-free sliding window; jump past the previous occurrence.
# Complexity: O(n) time, O(min(n, alphabet)) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        last = {}
        left = answer = 0
        for right, ch in enumerate(s):
            left = max(left, last.get(ch, -1) + 1)
            last[ch] = right
            answer = max(answer, right - left + 1)
        return answer
