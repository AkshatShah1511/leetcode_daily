# LeetCode 19: Remove Nth Node From End of List
# https://leetcode.com/problems/remove-nth-node-from-end-of-list/
# Imported: 2026-09-30.
# Approach: Separate two pointers by n nodes so the slower one stops before the removal.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def removeNthFromEnd(self, head, n: int):
        dummy = ListNode(0, head)
        slow = fast = dummy
        for _ in range(n): fast = fast.next
        while fast.next:
            slow, fast = slow.next, fast.next
        slow.next = slow.next.next
        return dummy.next
