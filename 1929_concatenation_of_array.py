# LeetCode 1929: Concatenation of Array
# https://leetcode.com/problems/concatenation-of-array/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Append the array to itself.
# Complexity: O(n) time and output space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def getConcatenation(self, nums: List[int]) -> List[int]:
        return nums+nums
