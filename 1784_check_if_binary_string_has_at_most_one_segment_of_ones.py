# LeetCode 1784: Check if Binary String Has at Most One Segment of Ones
# https://leetcode.com/problems/check-if-binary-string-has-at-most-one-segment-of-ones/
# Imported: 2026-09-30.
# Approach: With no leading zeros, a second ones segment exists exactly when 01 occurs.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def checkOnesSegment(self, s: str) -> bool:
        return '01' not in s
