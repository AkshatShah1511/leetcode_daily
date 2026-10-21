# LeetCode 22: Generate Parentheses
# https://leetcode.com/problems/generate-parentheses/
# Added: 2026-10-21 (Asia/Calcutta)
# Selection: Fallback; the official daily challenge could not be verified.
#
# Approach:
# Build each answer with backtracking. We may add an opening parenthesis while
# fewer than n have been used, and may add a closing parenthesis only when it
# can match an opening parenthesis already in the current prefix.
#
# Correctness:
# The rule closed < opened keeps every generated prefix valid, and a completed
# path contains exactly n opening and n closing parentheses, so every recorded
# string is well formed. Conversely, each well-formed string follows one valid
# sequence of these choices, so the search generates every answer exactly once.
#
# Time complexity: O(C_n * n), where C_n is the nth Catalan number.
# Space complexity: O(n) auxiliary space, excluding the returned strings.

from typing import List


class Solution:
    def generateParenthesis(self, n: int) -> List[str]:
        result: List[str] = []
        path: List[str] = []

        def backtrack(opened: int, closed: int) -> None:
            if len(path) == 2 * n:
                result.append("".join(path))
                return

            # Add an opening parenthesis while one of the n pairs remains.
            if opened < n:
                path.append("(")
                backtrack(opened + 1, closed)
                path.pop()

            # Closing is safe only when an unmatched opening parenthesis exists.
            if closed < opened:
                path.append(")")
                backtrack(opened, closed + 1)
                path.pop()

        backtrack(0, 0)
        return result
