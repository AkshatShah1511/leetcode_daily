# LeetCode 62: Unique Paths
# https://leetcode.com/problems/unique-paths/
# Added: 2026-10-18 (Asia/Calcutta)
# Selection: Fallback; today's official daily challenge could not be verified.
#
# Approach:
# Every valid path contains exactly m - 1 downward moves and n - 1 rightward
# moves. Therefore, the answer is the number of ways to choose where the less
# frequent kind of move appears among all m + n - 2 moves. Compute that binomial
# coefficient iteratively to use constant auxiliary space.
#
# Correctness:
# Mapping a path to its ordered sequence of down and right moves is one-to-one.
# Choosing the positions of all downward moves uniquely determines every right
# move, and vice versa, so the number of paths is C(m + n - 2, m - 1). The loop
# evaluates this binomial coefficient using its multiplicative formula, hence
# the returned value equals the number of unique valid paths.
#
# Time complexity: O(min(m, n)).
# Space complexity: O(1).


class Solution:
    def uniquePaths(self, m: int, n: int) -> int:
        total_moves = m + n - 2
        chosen_moves = min(m - 1, n - 1)
        paths = 1

        # After step i, paths equals C(total_moves - chosen_moves + i, i).
        for i in range(1, chosen_moves + 1):
            paths = paths * (total_moves - chosen_moves + i) // i

        return paths
