# LeetCode 138: Copy List with Random Pointer
# https://leetcode.com/problems/copy-list-with-random-pointer/
# Imported: 2026-09-30.
# Approach: Create every clone first, then connect its next and random pointers through a map.
# Complexity: O(n) time and space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def copyRandomList(self, head):
        copies = {None:None}
        node = head
        while node: copies[node] = Node(node.val); node = node.next
        node = head
        while node:
            copies[node].next = copies[node.next]
            copies[node].random = copies[node.random]
            node = node.next
        return copies[head]
