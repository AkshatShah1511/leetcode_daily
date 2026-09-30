# LeetCode 268: Missing Number
# https://leetcode.com/problems/missing-number/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Subtract the actual sum from the sum of all values from zero through n.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def missingNumber(self, nums: List[int]) -> int:
        n=len(nums)
        return n*(n+1)//2-sum(nums)
