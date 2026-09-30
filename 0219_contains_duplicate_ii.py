# LeetCode 219: Contains Duplicate II
# https://leetcode.com/problems/contains-duplicate-ii/
# Imported: 2026-09-30.
# Approach: The most recent equal value gives the smallest possible index gap.
# Complexity: O(n) expected time and space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        last = {}
        for i,x in enumerate(nums):
            if x in last and i-last[x] <= k: return True
            last[x] = i
        return False
