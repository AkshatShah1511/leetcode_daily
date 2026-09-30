# LeetCode 868: Binary Gap
# https://leetcode.com/problems/binary-gap/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Track positions of adjacent set bits while shifting the integer.
# Complexity: O(log n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def binaryGap(self, n: int) -> int:
        last=None; position=answer=0
        while n:
            if n&1:
                if last is not None: answer=max(answer,position-last)
                last=position
            n>>=1; position+=1
        return answer
