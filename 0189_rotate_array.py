# LeetCode 189: Rotate Array
# https://leetcode.com/problems/rotate-array/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Reverse the whole array, then reverse the two rotated segments.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def rotate(self, nums: List[int], k: int) -> None:
        if not nums: return
        k %= len(nums)
        def reverse(left,right):
            while left < right:
                nums[left],nums[right] = nums[right],nums[left]
                left += 1; right -= 1
        reverse(0,len(nums)-1); reverse(0,k-1); reverse(k,len(nums)-1)
