# LeetCode 424: Longest Repeating Character Replacement
# https://leetcode.com/problems/longest-repeating-character-replacement/
# Added: 2026-10-15 (Asia/Calcutta)
# Selection: Fallback; today's official daily challenge could not be verified.
#
# Approach:
# Maintain a sliding window and the frequency of each uppercase letter inside
# it. A window is valid when its length minus its most frequent letter count is
# at most k, because every other letter can be replaced by that frequent one.
# Expand the right edge, shrink the left edge until the window is valid again,
# and record the largest valid length.
#
# Correctness:
# For any current window, the fewest replacements needed to make all letters
# equal is window_length - maximum_frequency. The algorithm removes characters
# from the left exactly while that value exceeds k, so every recorded window
# can be made uniform with at most k replacements. Conversely, before each
# shrink the window is invalid, so it cannot be a feasible answer. Therefore,
# the largest recorded valid window is exactly the requested maximum length.
#
# Time complexity: O(26 * n) = O(n), where n is the length of s.
# Space complexity: O(26) = O(1).


class Solution:
    def characterReplacement(self, s: str, k: int) -> int:
        frequencies = [0] * 26
        left = 0
        best = 0

        for right, character in enumerate(s):
            frequencies[ord(character) - ord("A")] += 1

            # Shrink until all non-majority letters fit the replacement budget.
            while right - left + 1 - max(frequencies) > k:
                frequencies[ord(s[left]) - ord("A")] -= 1
                left += 1

            best = max(best, right - left + 1)

        return best
