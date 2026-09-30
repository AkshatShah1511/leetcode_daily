# LeetCode 136: Single Number
# https://leetcode.com/problems/single-number/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: XOR cancels equal pairs and leaves the unique value.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for x in nums: answer ^= x
        return answer
