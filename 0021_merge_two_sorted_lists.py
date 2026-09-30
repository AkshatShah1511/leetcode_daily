# LeetCode 21: Merge Two Sorted Lists
# https://leetcode.com/problems/merge-two-sorted-lists/
# Imported: 2026-09-30.
# Approach: Repeatedly attach the smaller list head; the merged prefix stays sorted.
# Complexity: O(m+n) time, O(1) auxiliary space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def mergeTwoLists(self, list1, list2):
        dummy = tail = ListNode(0)
        while list1 and list2:
            if list1.val <= list2.val:
                tail.next, list1 = list1, list1.next
            else:
                tail.next, list2 = list2, list2.next
            tail = tail.next
        tail.next = list1 or list2
        return dummy.next
