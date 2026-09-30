# LeetCode 1304: Find N Unique Integers Sum up to Zero
# https://leetcode.com/problems/find-n-unique-integers-sum-up-to-zero/
# Imported: 2026-09-30.
# Approach: Use opposite nonzero pairs and add zero only for odd n.
# Complexity: O(n) time and output space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def sumZero(self, n: int) -> List[int]:
        return [x for i in range(1,n//2+1) for x in (i,-i)]+([0] if n%2 else [])
