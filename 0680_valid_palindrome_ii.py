# LeetCode 680: Valid Palindrome II
# https://leetcode.com/problems/valid-palindrome-ii/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: At the first mismatch, any valid deletion must remove one of those two endpoints.
# Complexity: O(n) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def validPalindrome(self, s: str) -> bool:
        def check(left,right):
            while left<right:
                if s[left]!=s[right]: return False
                left+=1; right-=1
            return True
        left,right=0,len(s)-1
        while left<right:
            if s[left]!=s[right]: return check(left+1,right) or check(left,right-1)
            left+=1; right-=1
        return True
