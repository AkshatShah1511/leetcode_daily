# LeetCode 209: Minimum Size Subarray Sum
# https://leetcode.com/problems/minimum-size-subarray-sum/
# Imported: 2026-09-30.
# Approach: Positive values permit shrinking a qualifying window until it no longer qualifies.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        left = total = 0; answer = len(nums)+1
        for right,x in enumerate(nums):
            total += x
            while total >= target:
                answer = min(answer,right-left+1); total -= nums[left]; left += 1
        return answer if answer <= len(nums) else 0
