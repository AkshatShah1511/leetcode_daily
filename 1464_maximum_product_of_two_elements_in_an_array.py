# LeetCode 1464: Maximum Product of Two Elements in an Array
# https://leetcode.com/problems/maximum-product-of-two-elements-in-an-array/
# Imported: 2026-09-30.
# Approach: Positive values make the two largest elements optimal.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        first=second=0
        for x in nums:
            if x>=first: first,second=x,first
            elif x>second: second=x
        return (first-1)*(second-1)
