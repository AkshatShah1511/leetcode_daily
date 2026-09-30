# LeetCode 167: Two Sum II - Input Array Is Sorted
# https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/
# Imported: 2026-09-30.
# Approach: Sorted endpoints determine whether to raise the smaller or lower the larger value.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        left,right = 0,len(numbers)-1
        while left < right:
            total = numbers[left]+numbers[right]
            if total == target: return [left+1,right+1]
            if total < target: left += 1
            else: right -= 1
        return []
