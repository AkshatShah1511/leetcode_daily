# LeetCode 9: Palindrome Number
# https://leetcode.com/problems/palindrome-number/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Reverse only half the digits and compare the halves, skipping the middle digit.
# Complexity: O(log x) time, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def isPalindrome(self, x: int) -> bool:
        if x < 0 or (x % 10 == 0 and x != 0):
            return False
        half = 0
        while x > half:
            half = half * 10 + x % 10
            x //= 10
        return x == half or x == half // 10
