# LeetCode 567: Permutation in String
# https://leetcode.com/problems/permutation-in-string/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Compare counts for every window of the shorter string length.
# Complexity: O(n+m) time with fixed alphabet, O(1) space.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        need=[0]*26; window=[0]*26
        for ch in s1: need[ord(ch)-97]+=1
        for i,ch in enumerate(s2):
            window[ord(ch)-97]+=1
            if i>=len(s1): window[ord(s2[i-len(s1)])-97]-=1
            if i+1>=len(s1) and window==need: return True
        return False
