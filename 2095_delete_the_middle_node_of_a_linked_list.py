# LeetCode 2095: Delete the Middle Node of a Linked List
# https://leetcode.com/problems/delete-the-middle-node-of-a-linked-list/
# Imported: 2026-09-30.
# Approach: Fast/slow pointers identify the middle and its predecessor.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def deleteMiddle(self, head):
        if not head or not head.next: return None
        prev=None; slow=fast=head
        while fast and fast.next:
            prev,slow=slow,slow.next; fast=fast.next.next
        prev.next=slow.next
        return head
