# LeetCode 2348: Number of Zero-Filled Subarrays
# https://leetcode.com/problems/number-of-zero-filled-subarrays/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: A zero extending a run of length r adds r zero-filled subarrays ending here.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def zeroFilledSubarray(self, nums: List[int]) -> int:
        run=answer=0
        for x in nums:
            run=run+1 if x==0 else 0; answer+=run
        return answer
