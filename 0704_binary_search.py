# LeetCode 704: Binary Search
# https://leetcode.com/problems/binary-search/
# Imported: 2026-09-30.
# Approach: Compare the middle value and discard the impossible half.
# Complexity: O(log n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def search(self, nums: List[int], target: int) -> int:
        lo,hi=0,len(nums)-1
        while lo<=hi:
            mid=(lo+hi)//2
            if nums[mid]==target: return mid
            if nums[mid]<target: lo=mid+1
            else: hi=mid-1
        return -1
