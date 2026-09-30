# LeetCode 1200: Minimum Absolute Difference
# https://leetcode.com/problems/minimum-absolute-difference/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: A minimum-difference pair must be adjacent in sorted order.
# Complexity: O(n log n) time, O(n) sorting/output space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def minimumAbsDifference(self, arr: List[int]) -> List[List[int]]:
        arr.sort(); best=min(arr[i]-arr[i-1] for i in range(1,len(arr)))
        return [[arr[i-1],arr[i]] for i in range(1,len(arr)) if arr[i]-arr[i-1]==best]
