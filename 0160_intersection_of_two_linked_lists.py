# LeetCode 160: Intersection of Two Linked Lists
# https://leetcode.com/problems/intersection-of-two-linked-lists/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Switch each pointer to the other head; both traverse the same combined length.
# Complexity: O(m+n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def getIntersectionNode(self, headA, headB):
        a,b = headA,headB
        while a is not b:
            a = a.next if a else headB
            b = b.next if b else headA
        return a
