# LeetCode 1984: Minimum Difference Between Highest and Lowest of K Scores
# https://leetcode.com/problems/minimum-difference-between-highest-and-lowest-of-k-scores/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: The best k scores can be chosen as a consecutive sorted window.
# Complexity: O(n log n) time, O(n) sorting space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def minimumDifference(self, nums: List[int], k: int) -> int:
        nums.sort()
        return min(nums[i+k-1]-nums[i] for i in range(len(nums)-k+1))
