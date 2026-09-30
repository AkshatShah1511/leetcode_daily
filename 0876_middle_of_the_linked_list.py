# LeetCode 876: Middle of the Linked List
# https://leetcode.com/problems/middle-of-the-linked-list/
# Imported: 2026-09-30.
# Approach: A pointer moving once per two fast steps ends at the second middle.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def middleNode(self, head):
        slow=fast=head
        while fast and fast.next: slow,fast=slow.next,fast.next.next
        return slow
