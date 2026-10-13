# LeetCode 238: Product of Array Except Self
# https://leetcode.com/problems/product-of-array-except-self/
# Added: 2026-10-13 (Asia/Calcutta)
# Selection: Fallback; today's official daily challenge could not be verified.
#
# Approach:
# Store the product of every value to the left of each position in the result
# array. Then scan from right to left while maintaining the product of values
# to the right, and multiply that suffix product into each stored prefix.
#
# Correctness:
# After the first pass, result[i] equals the product of nums[0:i]. During the
# reverse pass, suffix equals the product of nums[i + 1:n] when result[i] is
# updated. Their product therefore contains every input value except nums[i],
# so every returned position is correct. This reasoning also covers zeros.
#
# Time complexity: O(n), where n is the length of nums.
# Space complexity: O(1) auxiliary space; the output array is not counted.

from typing import List


class Solution:
    def productExceptSelf(self, nums: List[int]) -> List[int]:
        result = [1] * len(nums)

        # result[i] becomes the product of all numbers before index i.
        prefix = 1
        for index, number in enumerate(nums):
            result[index] = prefix
            prefix *= number

        # Multiply by the product of all numbers after index i.
        suffix = 1
        for index in range(len(nums) - 1, -1, -1):
            result[index] *= suffix
            suffix *= nums[index]

        return result
