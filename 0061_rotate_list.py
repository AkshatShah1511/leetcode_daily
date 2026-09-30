# LeetCode 61: Rotate List
# https://leetcode.com/problems/rotate-list/
# Imported: 2026-09-30.
# Approach: Make a ring and cut it at length-k modulo length.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def rotateRight(self, head, k: int):
        if not head or not head.next: return head
        n, tail = 1, head
        while tail.next: tail = tail.next; n += 1
        k %= n
        if not k: return head
        tail.next = head
        for _ in range(n-k): tail = tail.next
        result = tail.next
        tail.next = None
        return result
