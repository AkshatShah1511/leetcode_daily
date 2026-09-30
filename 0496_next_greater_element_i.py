# LeetCode 496: Next Greater Element I
# https://leetcode.com/problems/next-greater-element-i/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: A decreasing stack resolves each value when its first larger successor arrives.
# Complexity: O(m+n) time, O(n) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def nextGreaterElement(self, nums1: List[int], nums2: List[int]) -> List[int]:
        stack=[]; greater={}
        for x in nums2:
            while stack and stack[-1] < x: greater[stack.pop()]=x
            stack.append(x)
        return [greater.get(x,-1) for x in nums1]
