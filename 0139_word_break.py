# LeetCode 139: Word Break
# https://leetcode.com/problems/word-break/
# Added: 2026-10-09 (Asia/Calcutta)
# Selection: Fallback; today's official daily challenge could not be verified.
#
# Approach:
# Use dynamic programming over prefixes. reachable[i] records whether s[:i]
# can be segmented using dictionary words. For each reachable endpoint, check
# only earlier split points within the longest dictionary-word length.
#
# Correctness:
# reachable[0] is true because the empty prefix needs no words. For each end,
# the algorithm marks reachable[end] true exactly when some reachable start
# exists and s[start:end] is a dictionary word. In that case, a valid
# segmentation of s[:start] followed by that word forms s[:end]. Conversely,
# every valid segmentation of s[:end] has a final dictionary word beginning
# at some start whose preceding prefix is segmentable, so the algorithm will
# find that split. Thus reachable[len(s)] is true exactly when all of s can
# be segmented.
#
# Complexity: O(n * L^2) time in Python due to substring creation, where L is
# the maximum word length, and O(n + D) space, where D is dictionary storage.

from typing import List


class Solution:
    def wordBreak(self, s: str, wordDict: List[str]) -> bool:
        words = set(wordDict)
        max_word_length = max(map(len, words))
        reachable = [False] * (len(s) + 1)
        reachable[0] = True

        for end in range(1, len(s) + 1):
            earliest_start = max(0, end - max_word_length)

            for start in range(earliest_start, end):
                if reachable[start] and s[start:end] in words:
                    reachable[end] = True
                    break

        return reachable[len(s)]
