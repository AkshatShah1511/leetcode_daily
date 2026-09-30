# LeetCode 24: Swap Nodes in Pairs
# https://leetcode.com/problems/swap-nodes-in-pairs/
# Imported: 2026-09-30.
# Approach: Rewire each adjacent pair while retaining the predecessor for reconnection.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def swapPairs(self, head):
        dummy = ListNode(0, head)
        prev = dummy
        while prev.next and prev.next.next:
            first, second = prev.next, prev.next.next
            first.next = second.next
            second.next = first
            prev.next = second
            prev = first
        return dummy.next
