# LeetCode 2: Add Two Numbers
# https://leetcode.com/problems/add-two-numbers/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Add aligned digits and carry; each output digit is the sum modulo ten.
# Complexity: O(m+n) time, O(m+n) output.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def addTwoNumbers(self, l1, l2):
        dummy = tail = ListNode(0)
        carry = 0
        while l1 or l2 or carry:
            total = carry
            if l1:
                total += l1.val
                l1 = l1.next
            if l2:
                total += l2.val
                l2 = l2.next
            carry, digit = divmod(total, 10)
            tail.next = ListNode(digit)
            tail = tail.next
        return dummy.next
