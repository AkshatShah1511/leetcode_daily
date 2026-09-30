# LeetCode 225: Implement Stack using Queues
# https://leetcode.com/problems/implement-stack-using-queues/
# Imported: 2026-09-30.
# Approach: After enqueueing, rotate earlier elements behind the new top using queue operations.
# Complexity: O(n) push, O(1) other operations, O(n) space.

from __future__ import annotations
from typing import List, Optional

from collections import deque
class MyStack:
    def __init__(self): self.queue = deque()
    def push(self, x: int) -> None:
        self.queue.append(x)
        for _ in range(len(self.queue)-1): self.queue.append(self.queue.popleft())
    def pop(self) -> int: return self.queue.popleft()
    def top(self) -> int: return self.queue[0]
    def empty(self) -> bool: return not self.queue
