# LeetCode 1323: Maximum 69 Number
# https://leetcode.com/problems/maximum-69-number/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Changing the leftmost six gives the largest positional increase.
# Complexity: O(d) time and space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def maximum69Number(self, num: int) -> int:
        return int(str(num).replace('6','9',1))
