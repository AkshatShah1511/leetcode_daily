# LeetCode 54: Spiral Matrix
# https://leetcode.com/problems/spiral-matrix/
# Added: 2026-10-26 (Asia/Calcutta)
# Selection: Fallback; the official daily challenge could not be verified.
#
# Approach:
# Maintain four boundaries around the unvisited rectangle. Traverse its top row,
# right column, bottom row, and left column, shrinking the matching boundary
# after each side. Before traversing the bottom or left side, check that the
# remaining rectangle still has that row or column to avoid duplicates.
#
# Correctness:
# At the start of each loop, the boundaries enclose exactly the unvisited cells.
# The four traversals append the outer layer clockwise, each cell once, and the
# boundary updates remove precisely that layer. The guarded reverse traversals
# handle a final single row or column without repeating cells. Therefore every
# matrix element is appended exactly once in spiral order.
#
# Time complexity: O(m * n), where m and n are the matrix dimensions.
# Space complexity: O(1) auxiliary space, excluding the returned list.

from typing import List


class Solution:
    def spiralOrder(self, matrix: List[List[int]]) -> List[int]:
        result: List[int] = []
        top, bottom = 0, len(matrix) - 1
        left, right = 0, len(matrix[0]) - 1

        while top <= bottom and left <= right:
            for column in range(left, right + 1):
                result.append(matrix[top][column])
            top += 1

            for row in range(top, bottom + 1):
                result.append(matrix[row][right])
            right -= 1

            if top <= bottom:
                for column in range(right, left - 1, -1):
                    result.append(matrix[bottom][column])
                bottom -= 1

            if left <= right:
                for row in range(bottom, top - 1, -1):
                    result.append(matrix[row][left])
                left += 1

        return result
