# LeetCode 744: Find Smallest Letter Greater Than Target
# https://leetcode.com/problems/find-smallest-letter-greater-than-target/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Upper bound finds the first strictly greater letter; wrap around when absent.
# Complexity: O(log n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

from bisect import bisect_right
class Solution:
    def nextGreatestLetter(self, letters: List[str], target: str) -> str:
        return letters[bisect_right(letters,target)%len(letters)]
