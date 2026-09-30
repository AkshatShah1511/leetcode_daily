# LeetCode 904: Fruit Into Baskets
# https://leetcode.com/problems/fruit-into-baskets/
# Imported: 2026-09-30.
# Approach: Maintain the longest window containing at most two fruit types.
# Complexity: O(n) expected time, O(1) space.

from __future__ import annotations
from typing import List, Optional

from collections import defaultdict
class Solution:
    def totalFruit(self, fruits: List[int]) -> int:
        counts=defaultdict(int); left=answer=0
        for right,x in enumerate(fruits):
            counts[x]+=1
            while len(counts)>2:
                y=fruits[left]; counts[y]-=1; left+=1
                if not counts[y]: del counts[y]
            answer=max(answer,right-left+1)
        return answer
