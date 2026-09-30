# LeetCode 1877: Minimize Maximum Pair Sum in Array
# https://leetcode.com/problems/minimize-maximum-pair-sum-in-array/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Pair smallest with largest; an exchange argument minimizes the worst pair sum.
# Complexity: O(n log n) time, O(n) sorting space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def minPairSum(self, nums: List[int]) -> int:
        nums.sort()
        return max(nums[i]+nums[-1-i] for i in range(len(nums)//2))
