# LeetCode 206: Reverse Linked List
# https://leetcode.com/problems/reverse-linked-list/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Reverse one next pointer at a time, preserving the unprocessed suffix.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def reverseList(self, head):
        prev = None
        while head:
            nxt = head.next; head.next = prev; prev,head = head,nxt
        return prev
