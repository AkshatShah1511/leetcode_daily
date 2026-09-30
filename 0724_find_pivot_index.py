# LeetCode 724: Find Pivot Index
# https://leetcode.com/problems/find-pivot-index/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Right sum equals total minus left sum minus the current value.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def pivotIndex(self, nums: List[int]) -> int:
        total=sum(nums); left=0
        for i,x in enumerate(nums):
            if left==total-left-x: return i
            left+=x
        return -1
