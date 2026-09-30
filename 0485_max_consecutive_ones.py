# LeetCode 485: Max Consecutive Ones
# https://leetcode.com/problems/max-consecutive-ones/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
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
