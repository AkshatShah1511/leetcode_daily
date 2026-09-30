# LeetCode 744: Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Imported: 2026-09-30.
# Approach: Upper bound finds the first strictly greater letter; wrap around when absent.
# Complexity: O(log n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

from bisect import bisect_right
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters,target)%len(letters)]
