# LeetCode 74: Search a 2D Matrix
# https://leetcode.com/problems/search-a-2d-matrix/
# Added: 2026-10-27 (Asia/Calcutta)
# Selection: Fallback; the official daily challenge could not be verified.
#
# Approach:
# Treat the matrix as one sorted array of length rows * columns and perform one
# binary search. A virtual index maps to matrix[index // columns][index % columns],
# so no flattened copy is needed.
#
# Correctness:
# Because every row is sorted and each row starts after the preceding row ends,
# the row-major virtual array is sorted. Binary search preserves the invariant
# that target, if present, lies between left and right. Comparing the midpoint
# discards only values that are strictly too small or too large. Therefore the
# method returns true exactly when target occurs in the matrix.
#
# Time complexity: O(log(m * n)).
# Space complexity: O(1).

from typing import List


class Solution:
    def searchMatrix(self, matrix: List[List[int]], target: int) -> bool:
        rows = len(matrix)
        columns = len(matrix[0])
        left, right = 0, rows * columns - 1

        while left <= right:
            middle = left + (right - left) // 2
            value = matrix[middle // columns][middle % columns]

            if value == target:
                return True
            if value < target:
                left = middle + 1
            else:
                right = middle - 1

        return False
