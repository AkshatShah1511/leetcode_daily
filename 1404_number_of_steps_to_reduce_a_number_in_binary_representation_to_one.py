# LeetCode 1404: Number of Steps to Reduce a Number in Binary Representation to One
# https://leetcode.com/problems/number-of-steps-to-reduce-a-number-in-binary-representation-to-one/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Scan bits right to left with carry; odd suffixes need increment then division.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def numSteps(self, s: str) -> int:
        carry=steps=0
        for i in range(len(s)-1,0,-1):
            if int(s[i])+carry==1: steps+=2; carry=1
            else: steps+=1
        return steps+carry
