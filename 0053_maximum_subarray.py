# LeetCode 53: Maximum Subarray
# https://leetcode.com/problems/maximum-subarray/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Kadane: the best subarray ending here either extends the previous one or restarts.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        ending = answer = nums[0]
        for index in range(1,len(nums)):
            x = nums[index]
            ending = max(x,ending+x)
            answer = max(answer,ending)
        return answer
