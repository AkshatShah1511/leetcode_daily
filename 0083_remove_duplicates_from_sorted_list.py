# LeetCode 83: Remove Duplicates from Sorted List
# https://leetcode.com/problems/remove-duplicates-from-sorted-list/
# Imported: 2026-09-30.
# Approach: Equal values are adjacent; bypass repeated successors.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def deleteDuplicates(self, head):
        node = head
        while node and node.next:
            if node.val == node.next.val: node.next = node.next.next
            else: node = node.next
        return head
