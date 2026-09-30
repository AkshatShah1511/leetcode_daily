# LeetCode 3912: Valid Elements in an Array
# https://leetcode.com/problems/valid-elements-in-an-array/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Mark strict record highs from each direction, then emit marked entries in order.
# Complexity: O(n) time and space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def findValidElements(self, nums: List[int]) -> List[int]:
        valid=[False]*len(nums); maximum=float('-inf')
        for i,x in enumerate(nums):
            if x>maximum: valid[i]=True
            maximum=max(maximum,x)
        maximum=float('-inf')
        for i in range(len(nums)-1,-1,-1):
            if nums[i]>maximum: valid[i]=True
            maximum=max(maximum,nums[i])
        return [x for i,x in enumerate(nums) if valid[i]]
