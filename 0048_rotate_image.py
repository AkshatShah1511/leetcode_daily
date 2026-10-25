# LeetCode 48: Rotate Image
# https://leetcode.com/problems/rotate-image/
# Added: 2026-10-25 (Asia/Calcutta)
# Selection: Fallback; the official daily challenge could not be verified.
#
# Approach:
# Rotate the square matrix in place in two steps. First transpose it across the
# main diagonal, exchanging matrix[row][column] with matrix[column][row]. Then
# reverse every row. The composition is a 90-degree clockwise rotation.
#
# Correctness:
# Transposition moves the original element at (row, column) to (column, row).
# Reversing that destination row changes its column from row to n - 1 - row.
# Thus every original element ends at (column, n - 1 - row), exactly its
# position after a 90-degree clockwise rotation. Since swaps are in place, the
# entire input matrix is rotated without allocating another matrix.
#
# Time complexity: O(n^2), where n is the matrix side length.
# Space complexity: O(1).

from typing import List


class Solution:
    def rotate(self, matrix: List[List[int]]) -> None:
        """Rotate matrix 90 degrees clockwise in place; return nothing."""
        size = len(matrix)

        # Transpose only entries above the diagonal to avoid swapping twice.
        for row in range(size):
            for column in range(row + 1, size):
                matrix[row][column], matrix[column][row] = (
                    matrix[column][row],
                    matrix[row][column],
                )

        # Mirroring each transposed row completes the clockwise rotation.
        for row in matrix:
            row.reverse()
