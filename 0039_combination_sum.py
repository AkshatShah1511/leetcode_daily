# LeetCode 39: Combination Sum
# https://leetcode.com/problems/combination-sum/
# Added: 2026-10-20 (Asia/Calcutta)
# Selection: Fallback; today's official daily challenge could not be verified.
#
# Approach:
# Sort the candidates and build combinations with backtracking. At each step,
# consider only candidates at or after a start index. Recurse with the same
# index when choosing a value so it may be reused, and stop once candidates are
# larger than the remaining target.
#
# Correctness:
# Every generated path is nondecreasing because recursion never moves before
# its start index, so the same multiset cannot be produced in different orders.
# Choosing a candidate subtracts it from the remaining target, and a path is
# recorded only when that remainder is zero, so every result is valid. For any
# valid combination, its sorted values follow one available recursion branch,
# including repeated choices at the same index, so every valid combination is
# generated. Therefore the output contains all and only unique valid sums.
#
# Time complexity: O(n^(target / minimum_candidate)) in the worst case.
# Space complexity: O(target / minimum_candidate) excluding the output.

from typing import List


class Solution:
    def combinationSum(self, candidates: List[int], target: int) -> List[List[int]]:
        ordered = sorted(candidates)
        combinations: List[List[int]] = []
        current: List[int] = []

        def backtrack(start: int, remaining: int) -> None:
            if remaining == 0:
                combinations.append(current.copy())
                return

            for index in range(start, len(ordered)):
                value = ordered[index]
                if value > remaining:
                    break

                current.append(value)
                # Reuse is allowed, so the next choice may use this index again.
                backtrack(index, remaining - value)
                current.pop()

        backtrack(0, target)
        return combinations
