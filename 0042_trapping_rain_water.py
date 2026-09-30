# LeetCode 42: Trapping Rain Water
# https://leetcode.com/problems/trapping-rain-water/
# Imported: 2026-09-30.
# Approach: Process the smaller boundary; its running maximum determines the trapped water.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def trap(self, height: List[int]) -> int:
        left, right = 0, len(height)-1
        lm = rm = answer = 0
        while left <= right:
            if height[left] <= height[right]:
                lm = max(lm,height[left]); answer += lm-height[left]; left += 1
            else:
                rm = max(rm,height[right]); answer += rm-height[right]; right -= 1
        return answer
