# LeetCode 136: Single Number
# https://leetcode.com/problems/single-number/
# Imported: 2026-09-30.
# Approach: XOR cancels equal pairs and leaves the unique value.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def singleNumber(self, nums: List[int]) -> int:
        answer = 0
        for x in nums: answer ^= x
        return answer
