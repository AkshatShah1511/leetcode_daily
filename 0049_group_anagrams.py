# LeetCode 49: Group Anagrams
# https://leetcode.com/problems/group-anagrams/
# Imported: 2026-09-30.
# Approach: Anagrams share the same 26-letter count tuple.
# Complexity: O(total characters) time, O(total characters) output and grouping space.

from __future__ import annotations
from typing import List, Optional

from collections import defaultdict
class Solution:
    def groupAnagrams(self, strs: List[str]) -> List[List[str]]:
        groups = defaultdict(list)
        for word in strs:
            counts = [0]*26
            for ch in word: counts[ord(ch)-97] += 1
            groups[tuple(counts)].append(word)
        return list(groups.values())
