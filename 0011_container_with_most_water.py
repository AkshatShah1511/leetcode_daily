# LeetCode 11: Container With Most Water
# https://leetcode.com/problems/container-with-most-water/
# Imported: 2026-09-30.
# Approach: Move the shorter boundary; retaining it with less width cannot improve the area.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def maxArea(self, height: List[int]) -> int:
        left, right, answer = 0, len(height) - 1, 0
        while left < right:
            answer = max(answer, (right-left)*min(height[left], height[right]))
            if height[left] < height[right]: left += 1
            else: right -= 1
        return answer
