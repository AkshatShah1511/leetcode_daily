# LeetCode 155: Min Stack
# https://leetcode.com/problems/min-stack/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Store the minimum so far alongside every pushed value.
# Complexity: O(1) per operation, O(n) space.

from __future__ import annotations
from typing import List, Optional

class MinStack:
    def __init__(self): self.stack = []
    def push(self, val: int) -> None:
        self.stack.append((val,min(val,self.stack[-1][1]) if self.stack else val))
    def pop(self) -> None: self.stack.pop()
    def top(self) -> int: return self.stack[-1][0]
    def getMin(self) -> int: return self.stack[-1][1]
