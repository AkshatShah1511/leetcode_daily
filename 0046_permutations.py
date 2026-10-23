# LeetCode 46: Permutations
# https://leetcode.com/problems/permutations/
# Added: 2026-10-23 (Asia/Calcutta)
# Selection: Fallback; the official daily challenge could not be verified.
#
# Approach:
# Use backtracking and build one permutation from left to right. A boolean list
# records which input positions are already present in the current path. At
# each step, try every unused number, recurse, and undo the choice afterward.
#
# Correctness:
# Every completed path contains each input number exactly once because a number
# can be chosen only while its position is unused, and completion occurs only
# after n choices. Conversely, any permutation determines one unique sequence
# of choices in the search tree. Therefore the algorithm returns every valid
# permutation exactly once and returns no invalid result.
#
# Time complexity: O(n * n!) to construct all n! permutations of length n.
# Space complexity: O(n) auxiliary space, excluding the returned permutations.

from typing import List


class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:
        result: List[List[int]] = []
        path: List[int] = []
        used = [False] * len(nums)

        def backtrack() -> None:
            if len(path) == len(nums):
                result.append(path.copy())
                return

            for index, number in enumerate(nums):
                if used[index]:
                    continue

                used[index] = True
                path.append(number)
                backtrack()
                path.pop()
                used[index] = False

        backtrack()
        return result
