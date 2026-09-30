# LeetCode 141: Linked List Cycle
# https://leetcode.com/problems/linked-list-cycle/
# Imported: 2026-09-30.
# Approach: Floyd pointers meet inside a cycle; otherwise the fast pointer reaches the end.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def hasCycle(self, head) -> bool:
        slow = fast = head
        while fast and fast.next:
            slow,fast = slow.next,fast.next.next
            if slow is fast: return True
        return False
