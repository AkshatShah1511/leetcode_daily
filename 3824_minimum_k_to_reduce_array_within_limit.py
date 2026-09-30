# LeetCode 3824: Minimum K to Reduce Array Within Limit
# https://leetcode.com/problems/minimum-k-to-reduce-array-within-limit/
# Imported: 2026-09-30.
# Approach: Binary-search k: sum(ceil(x/k)) decreases while k squared increases.
# Complexity: O(n log(max(max(nums),n))) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def minimumK(self, nums: List[int]) -> int:
        lo,hi=1,max(max(nums),len(nums))
        while lo<hi:
            mid=(lo+hi)//2
            if sum((x+mid-1)//mid for x in nums)<=mid*mid: hi=mid
            else: lo=mid+1
        return lo
