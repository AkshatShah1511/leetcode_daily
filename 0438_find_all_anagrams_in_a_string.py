# LeetCode 438: Find All Anagrams in a String
# https://leetcode.com/problems/find-all-anagrams-in-a-string/
# Fresh Python solution for the user's solved-question archive.
# Imported: 2026-09-30. Not the user's original submission.
# Approach: Compare 26-letter counts for each window of pattern length.
# Complexity: O(n+m) time with fixed alphabet, O(1) auxiliary space plus output.

from __future__ import annotations
from typing import List, Optional

class Solution:
    def findAnagrams(self, s: str, p: str) -> List[int]:
        need=[0]*26; window=[0]*26; answer=[]
        for ch in p: need[ord(ch)-97]+=1
        for i,ch in enumerate(s):
            window[ord(ch)-97]+=1
            if i >= len(p): window[ord(s[i-len(p)])-97]-=1
            if i+1 >= len(p) and window == need: answer.append(i-len(p)+1)
        return answer
