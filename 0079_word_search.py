# LeetCode 79: Word Search
# https://leetcode.com/problems/word-search/
# Added: 2026-10-19 (Asia/Calcutta)
# Selection: Fallback; today's official daily challenge could not be verified.
#
# Approach:
# First reject words requiring more copies of a letter than the board contains.
# Then run backtracking from every cell: match the next character, mark the cell
# as used, and try its four neighbors. Start from the rarer end of the word to
# reduce the number of initial search branches.
#
# Correctness:
# Each recursive state represents one path of distinct adjacent cells matching
# word[0:index]. A recursive step visits exactly every unused horizontal or
# vertical neighbor that matches word[index], so it generates every valid next
# path and no invalid path. Reaching index == len(word) proves a complete match.
# Trying every starting cell therefore returns True exactly when some valid path
# spells the word; reversing the word does not change whether such a path exists.
#
# Time complexity: O(m * n * 3^L) in the worst case, for word length L.
# Space complexity: O(L) for recursion and the visited cells.

from collections import Counter
from typing import List, Set, Tuple


class Solution:
    def exist(self, board: List[List[str]], word: str) -> bool:
        rows, columns = len(board), len(board[0])
        board_counts = Counter(character for row in board for character in row)
        word_counts = Counter(word)

        if any(board_counts[character] < needed for character, needed in word_counts.items()):
            return False

        # Starting with the rarer endpoint usually prunes failed searches sooner.
        if board_counts[word[-1]] < board_counts[word[0]]:
            word = word[::-1]

        visited: Set[Tuple[int, int]] = set()

        def search(row: int, column: int, index: int) -> bool:
            if index == len(word):
                return True
            if (
                row < 0
                or row >= rows
                or column < 0
                or column >= columns
                or (row, column) in visited
                or board[row][column] != word[index]
            ):
                return False

            visited.add((row, column))
            found = (
                search(row + 1, column, index + 1)
                or search(row - 1, column, index + 1)
                or search(row, column + 1, index + 1)
                or search(row, column - 1, index + 1)
            )
            visited.remove((row, column))
            return found

        return any(search(row, column, 0) for row in range(rows) for column in range(columns))
