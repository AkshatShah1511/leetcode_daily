# LeetCode 713: Subarray Product Less Than K
# https://leetcode.com/problems/subarray-product-less-than-k/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: For positive values, shrink until product<k; every suffix of the window qualifies.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def numSubarrayProductLessThanK(self, nums: List[int], k: int) -> int:
        if k<=1: return 0
        product=1; left=answer=0
        for right,x in enumerate(nums):
            product*=x
            while product>=k: product//=nums[left]; left+=1
            answer+=right-left+1
        return answer
