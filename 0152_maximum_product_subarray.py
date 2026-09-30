# LeetCode 152: Maximum Product Subarray
# https://leetcode.com/problems/maximum-product-subarray/
# Imported: 2026-09-30.
# Approach: Track both extreme ending products because a negative factor exchanges their roles.
# Complexity: O(n) time, O(1) auxiliary space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        low = high = answer = nums[0]
        for i in range(1,len(nums)):
            x = nums[i]
            low,high = min(x,x*low,x*high),max(x,x*low,x*high)
            answer = max(answer,high)
        return answer
