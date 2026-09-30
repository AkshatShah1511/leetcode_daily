# LeetCode 283: Move Zeroes
# https://leetcode.com/problems/move-zeroes/
# Imported: 2026-09-30.
# Approach: Compact nonzeros in order, then fill the remaining suffix with zeros.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def moveZeroes(self, nums: List[int]) -> None:
        write=0
        for x in nums:
            if x: nums[write]=x; write+=1
        for i in range(write,len(nums)): nums[i]=0
