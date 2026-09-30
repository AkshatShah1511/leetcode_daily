# LeetCode 2540: Minimum Common Value
# https://leetcode.com/problems/minimum-common-value/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Advance the smaller sorted value until both pointers agree.
# Complexity: O(m+n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def getCommon(self, nums1: List[int], nums2: List[int]) -> int:
        i=j=0
        while i<len(nums1) and j<len(nums2):
            if nums1[i]==nums2[j]: return nums1[i]
            if nums1[i]<nums2[j]: i+=1
            else: j+=1
        return -1
