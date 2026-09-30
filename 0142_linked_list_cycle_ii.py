# LeetCode 142: Linked List Cycle II
# https://leetcode.com/problems/linked-list-cycle-ii/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: After a Floyd meeting, equal-speed pointers from head and meeting meet at the entry.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def detectCycle(self, head):
        slow = fast = head
        while fast and fast.next:
            slow,fast = slow.next,fast.next.next
            if slow is fast:
                entry = head
                while entry is not slow: entry,slow = entry.next,slow.next
                return entry
        return None
