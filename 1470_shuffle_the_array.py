# LeetCode 1470: Shuffle the Array
# https://leetcode.com/problems/shuffle-the-array/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Interleave the corresponding entries of the two halves.
# Complexity: O(n) time and output space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def shuffle(self, nums: List[int], n: int) -> List[int]:
        return [value for i in range(n) for value in (nums[i],nums[n+i])]
