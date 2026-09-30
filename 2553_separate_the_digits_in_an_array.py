# LeetCode 2553: Separate the Digits in an Array
# https://leetcode.com/problems/separate-the-digits-in-an-array/
# Imported: 2026-09-30.
# Approach: Emit each integer digit in its original left-to-right order.
# Complexity: O(total digits) time and output space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def separateDigits(self, nums: List[int]) -> List[int]:
        return [int(ch) for x in nums for ch in str(x)]
