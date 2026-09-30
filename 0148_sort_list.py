# LeetCode 148: Sort List
# https://leetcode.com/problems/sort-list/
# Imported: 2026-09-30.
# Approach: Split the list in half, recursively sort both halves, and merge sorted lists.
# Complexity: O(n log n) time, O(log n) recursion space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def sortList(self, head):
        if not head or not head.next: return head
        slow,fast = head,head.next
        while fast and fast.next: slow,fast = slow.next,fast.next.next
        right = slow.next; slow.next = None
        left,right = self.sortList(head),self.sortList(right)
        dummy = tail = ListNode(0)
        while left and right:
            if left.val <= right.val: tail.next,left = left,left.next
            else: tail.next,right = right,right.next
            tail = tail.next
        tail.next = left or right
        return dummy.next
