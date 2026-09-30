# LeetCode 594: Longest Harmonious Subsequence
# https://leetcode.com/problems/longest-harmonious-subsequence/
# Imported: 2026-09-30.
# Approach: A harmonious subsequence uses only x and x+1, with both present.
# Complexity: O(n) expected time and space.

from __future__ import annotations
from typing import List, Optional

from collections import Counter
class Solution:
    def findLHS(self, nums: List[int]) -> int:
        counts=Counter(nums)
        return max((count+counts[x+1] for x,count in counts.items() if x+1 in counts),default=0)
