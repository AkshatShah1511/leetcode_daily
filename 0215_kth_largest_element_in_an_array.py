# LeetCode 215: Kth Largest Element in an Array
# https://leetcode.com/problems/kth-largest-element-in-an-array/
# Added: 2026-10-11 (Asia/Calcutta)
# Selection: Fallback; today's official daily challenge could not be verified.
#
# Approach:
# Maintain a min-heap containing the k largest values seen so far. Push each
# value, and whenever the heap grows beyond k, remove its smallest value.
# The heap's root is then the smallest among the retained k values.
#
# Correctness:
# After processing any prefix, the heap contains exactly the k largest values
# of that prefix, or every value if fewer than k have been seen. This holds
# initially. Adding the next value and removing the smallest when necessary
# leaves precisely the k largest values of the expanded prefix, preserving the
# invariant. After all values are processed, the heap contains the array's k
# largest values, so its smallest value is exactly the kth largest element.
#
# Complexity: O(n log k) time and O(k) auxiliary space.

import heapq
from typing import List


class Solution:
    def findKthLargest(self, nums: List[int], k: int) -> int:
        largest: List[int] = []

        for number in nums:
            heapq.heappush(largest, number)

            if len(largest) > k:
                heapq.heappop(largest)

        return largest[0]
