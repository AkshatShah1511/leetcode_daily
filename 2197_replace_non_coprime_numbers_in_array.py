# LeetCode 2197: Replace Non-Coprime Numbers in Array
# https://leetcode.com/problems/replace-non-coprime-numbers-in-array/
# Imported: 2026-09-30.
# Approach: Maintain a coprime-adjacent stack; merge its top repeatedly with the incoming LCM.
# Complexity: O(n log M) arithmetic time, O(n) space.

from __future__ import annotations
from typing import List, Optional

from math import gcd
class Solution:
    def replaceNonCoprimes(self, nums: List[int]) -> List[int]:
        stack=[]
        for x in nums:
            while stack:
                g=gcd(stack[-1],x)
                if g==1: break
                x=stack.pop()//g*x
            stack.append(x)
        return stack
