# LeetCode 234: Palindrome Linked List
# https://leetcode.com/problems/palindrome-linked-list/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Reverse the second half, compare halves, then restore the original list.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def isPalindrome(self, head) -> bool:
        if not head or not head.next: return True
        slow=fast=head
        while fast.next and fast.next.next: slow,fast=slow.next,fast.next.next
        def reverse(node):
            prev=None
            while node:
                nxt=node.next; node.next=prev; prev,node=node,nxt
            return prev
        second=reverse(slow.next)
        a,b,answer=head,second,True
        while b:
            if a.val != b.val: answer=False
            a,b=a.next,b.next
        slow.next=reverse(second)
        return answer
