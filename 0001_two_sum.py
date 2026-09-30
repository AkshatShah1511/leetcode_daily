# LeetCode 1: Two Sum
# https://leetcode.com/problems/two-sum/
# Added: 2026-09-30
# Selection: starter problem; not verified as the official daily challenge.
#
# Approach:
# Scan the array once, remembering each earlier value and its index.
# For each number, check whether target - number has already appeared.
# If it has, those two indices form the answer. Check before inserting
# the current number so that the same element is never used twice.
#
# Correctness:
# Before each iteration, seen contains only indices before the current one.
# Any returned pair therefore uses distinct indices and sums to target.
# When we reach the later element of the guaranteed pair, its complement
# is already in seen, so the algorithm finds a valid answer.
#
# Complexity: O(n) expected time and O(n) extra space.

from typing import List


class Solution:
    def twoSum(self, nums: List[int], target: int) -> List[int]:
        seen = {}
        for index, number in enumerate(nums):
            complement = target - number
            if complement in seen:
                return [seen[complement], index]
            # Store this number for subsequent elements to match against.
            seen[number] = index

        # LeetCode guarantees a solution; this handles invalid inputs explicitly.
        raise ValueError("No pair sums to the target")
