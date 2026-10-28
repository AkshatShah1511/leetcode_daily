# LeetCode 73: Set Matrix Zeroes
# https://leetcode.com/problems/set-matrix-zeroes/
# Added: 2026-10-28 (Asia/Calcutta)
# Selection: Fallback; the official daily challenge could not be verified.
#
# Approach:
# Use the first row and first column as in-place marker arrays. Two booleans
# separately remember whether those marker row/column originally contained a
# zero. Mark zeros found in the remaining cells, zero their indicated rows and
# columns, then handle the first row and first column last.
#
# Correctness:
# For every interior zero, its row marker and column marker are set, so the
# second pass zeros every cell sharing that original zero's row or column.
# Conversely, a marker is set only because its corresponding row or column had
# an original zero, so no unrelated interior cell is cleared. The two saved
# booleans apply the same rule to the first row and first column. Therefore the
# final matrix has zeros exactly in all required rows and columns.
#
# Time complexity: O(m * n), where m and n are the matrix dimensions.
# Space complexity: O(1).

from typing import List


class Solution:
    def setZeroes(self, matrix: List[List[int]]) -> None:
        """Modify matrix in place; return nothing."""
        rows = len(matrix)
        columns = len(matrix[0])
        first_row_zero = any(matrix[0][column] == 0 for column in range(columns))
        first_column_zero = any(matrix[row][0] == 0 for row in range(rows))

        # Store row and column markers in the matrix itself.
        for row in range(1, rows):
            for column in range(1, columns):
                if matrix[row][column] == 0:
                    matrix[row][0] = 0
                    matrix[0][column] = 0

        # Apply markers to every non-marker cell.
        for row in range(1, rows):
            for column in range(1, columns):
                if matrix[row][0] == 0 or matrix[0][column] == 0:
                    matrix[row][column] = 0

        if first_row_zero:
            for column in range(columns):
                matrix[0][column] = 0

        if first_column_zero:
            for row in range(rows):
                matrix[row][0] = 0
