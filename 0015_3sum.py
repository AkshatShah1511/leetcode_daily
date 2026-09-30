# LeetCode 15: 3Sum
# https://leetcode.com/problems/3sum/
# Imported: 2026-09-30.
# Approach: Sort, fix one element, and use two pointers; skip equal values to avoid duplicates.
# Complexity: O(n^2) time, O(n) sorting space plus output.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def threeSum(self, nums: List[int]) -> List[List[int]]:
        nums.sort()
        answer = []
        for i in range(len(nums)-2):
            if i and nums[i] == nums[i-1]: continue
            if nums[i] > 0: break
            left, right = i+1, len(nums)-1
            while left < right:
                total = nums[i]+nums[left]+nums[right]
                if total < 0: left += 1
                elif total > 0: right -= 1
                else:
                    answer.append([nums[i],nums[left],nums[right]])
                    left += 1
                    right -= 1
                    while left < right and nums[left] == nums[left-1]: left += 1
                    while left < right and nums[right] == nums[right+1]: right -= 1
        return answer
