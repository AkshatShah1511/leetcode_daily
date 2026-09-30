# LeetCode 560: Subarray Sum Equals K
# https://leetcode.com/problems/subarray-sum-equals-k/
# Imported: 2026-09-30.
# Approach: Count earlier prefix sums equal to current_sum-k; each gives one valid subarray.
# Complexity: O(n) expected time and space.

from __future__ import annotations
from typing import List, Optional

from collections import defaultdict
class Solution:
    def subarraySum(self, nums: List[int], k: int) -> int:
        counts=defaultdict(int,{0:1}); total=answer=0
        for x in nums:
            total+=x; answer+=counts[total-k]; counts[total]+=1
        return answer
