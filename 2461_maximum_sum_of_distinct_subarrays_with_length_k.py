# LeetCode 2461: Maximum Sum of Distinct Subarrays With Length K
# https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Track sum and frequencies for fixed-length windows; k distinct keys means valid.
# Complexity: O(n) expected time, O(k) space.

from __future__ import annotations
from typing import List, Optional

from collections import defaultdict
class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        counts=defaultdict(int); total=answer=0
        for i,x in enumerate(nums):
            counts[x]+=1; total+=x
            if i>=k:
                old=nums[i-k]; counts[old]-=1; total-=old
                if counts[old]==0: del counts[old]
            if i+1>=k and len(counts)==k: answer=max(answer,total)
        return answer
