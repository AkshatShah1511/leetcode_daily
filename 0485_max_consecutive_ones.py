# LeetCode 485: Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/
# Imported: 2026-09-30.
# Approach: Count the current run of ones, resetting on each zero.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def findMaxConsecutiveOnes(self, nums: List[int]) -> int:
        run=answer=0
        for x in nums:
            run=run+1 if x else 0; answer=max(answer,run)
        return answer
