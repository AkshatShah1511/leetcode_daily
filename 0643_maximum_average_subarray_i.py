# LeetCode 643: Maximum Average Subarray I
# https://leetcode.com/problems/maximum-average-subarray-i/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Maintain the sum of a fixed-length window by adding and removing its endpoints.
# Complexity: O(n) time, O(1) auxiliary space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        total=sum(nums[i] for i in range(k)); best=total
        for i in range(k,len(nums)):
            total+=nums[i]-nums[i-k]; best=max(best,total)
        return best/k
