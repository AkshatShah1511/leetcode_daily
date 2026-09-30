# LeetCode 268: Missing Number
# https://leetcode.com/problems/missing-number/
# Imported: 2026-09-30.
# Approach: Subtract the actual sum from the sum of all values from zero through n.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        return n*(n+1)//2-sum(nums)
