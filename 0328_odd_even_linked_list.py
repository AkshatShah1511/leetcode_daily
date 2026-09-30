# LeetCode 328: Odd Even Linked List
# https://leetcode.com/problems/odd-even-linked-list/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Build odd-position and even-position chains, then append the even chain.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def oddEvenList(self, head):
        if not head: return head
        odd,even=head,head.next; even_head=even
        while even and even.next:
            odd.next=even.next; odd=odd.next
            even.next=odd.next; even=even.next
        odd.next=even_head
        return head
