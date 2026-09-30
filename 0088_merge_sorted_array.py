# LeetCode 88: Merge Sorted Array
# https://leetcode.com/problems/merge-sorted-array/
# Imported: 2026-09-30.
# Approach: Merge backward so unread elements of nums1 are never overwritten.
# Complexity: O(m+n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        i,j,k = m-1,n-1,m+n-1
        while j >= 0:
            if i >= 0 and nums1[i] > nums2[j]: nums1[k] = nums1[i]; i -= 1
            else: nums1[k] = nums2[j]; j -= 1
            k -= 1
