# LeetCode 55: Jump Game
# https://leetcode.com/problems/jump-game/
# Added: 2026-10-24 (Asia/Calcutta)
# Selection: Fallback; the official daily challenge could not be verified.
#
# Approach:
# Scan from left to right while storing the farthest index reachable so far.
# If the current index is beyond that boundary, it cannot be reached and the
# answer is false. Otherwise, extend the boundary using the current jump length.
# Stop early as soon as the boundary reaches the final index.
#
# Correctness:
# Before each iteration, farthest is the greatest index reachable using only
# positions already scanned. If index <= farthest, that index is reachable, so
# every position through index + nums[index] is also reachable and updating the
# boundary is valid. If index > farthest, no earlier reachable position can jump
# to it, so neither it nor any later position can be reached. Thus the algorithm
# returns true exactly when the last index is reachable.
#
# Time complexity: O(n), where n is the length of nums.
# Space complexity: O(1).

from typing import List


class Solution:
    def canJump(self, nums: List[int]) -> bool:
        farthest = 0
        last_index = len(nums) - 1

        for index, jump_length in enumerate(nums):
            if index > farthest:
                return False

            farthest = max(farthest, index + jump_length)
            if farthest >= last_index:
                return True

        return False
