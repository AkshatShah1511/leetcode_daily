# LeetCode 1004: Max Consecutive Ones III
# https://leetcode.com/problems/max-consecutive-ones-iii/
# Imported: 2026-09-30.
# Approach: A sliding window is valid while it contains at most k zeros.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def longestOnes(self, nums: List[int], k: int) -> int:
        left=zeros=answer=0
        for right,x in enumerate(nums):
            zeros+=x==0
            while zeros>k: zeros-=nums[left]==0; left+=1
            answer=max(answer,right-left+1)
        return answer
