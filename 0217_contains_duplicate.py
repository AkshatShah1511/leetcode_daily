# LeetCode 217: Contains Duplicate
# https://leetcode.com/problems/contains-duplicate/
# Imported: 2026-09-30.
# Approach: A set removes duplicates; compare its size to the input.
# Complexity: O(n) expected time and space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        return len(set(nums)) != len(nums)
