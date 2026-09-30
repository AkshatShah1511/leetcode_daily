# LeetCode 17: Letter Combinations of a Phone Number
# https://leetcode.com/problems/letter-combinations-of-a-phone-number/
# Imported: 2026-09-30.
# Approach: Extend every partial combination with each letter for the next digit.
# Complexity: O(n*4^n) time and output space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def letterCombinations(self, digits: str) -> List[str]:
        if not digits: return []
        keys = {'2':'abc','3':'def','4':'ghi','5':'jkl','6':'mno','7':'pqrs','8':'tuv','9':'wxyz'}
        result = ['']
        for digit in digits:
            result = [prefix+ch for prefix in result for ch in keys[digit]]
        return result
