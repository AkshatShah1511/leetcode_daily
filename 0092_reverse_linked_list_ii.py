# LeetCode 92: Reverse Linked List II
# https://leetcode.com/problems/reverse-linked-list-ii/
# Imported: 2026-09-30.
# Approach: Move each next node to the front of the selected segment.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def reverseBetween(self, head, left: int, right: int):
        dummy = ListNode(0,head)
        before = dummy
        for _ in range(left-1): before = before.next
        tail = before.next
        for _ in range(right-left):
            node = tail.next
            tail.next = node.next
            node.next = before.next
            before.next = node
        return dummy.next
