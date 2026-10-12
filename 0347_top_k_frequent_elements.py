# LeetCode 347: Top K Frequent Elements
# https://leetcode.com/problems/top-k-frequent-elements/
# Added: 2026-10-12 (Asia/Calcutta)
# Selection: Fallback; today's official daily challenge could not be verified.
#
# Approach:
# Count each value, then place it into a bucket indexed by its frequency.
# Scan the buckets from highest frequency to lowest and collect values until
# exactly k values have been selected.
#
# Correctness:
# Every distinct value is stored in the bucket whose index equals its exact
# frequency. Because buckets are scanned in decreasing index order, every
# collected value is at least as frequent as every value not yet considered.
# The problem guarantees a unique answer, so once k values are collected,
# they are precisely the k most frequent elements. Therefore the returned
# list is correct.
#
# Complexity: O(n) time and O(n) auxiliary space.

from collections import Counter
from typing import List


class Solution:
    def topKFrequent(self, nums: List[int], k: int) -> List[int]:
        frequencies = Counter(nums)
        buckets: List[List[int]] = [[] for _ in range(len(nums) + 1)]

        for number, frequency in frequencies.items():
            buckets[frequency].append(number)

        result: List[int] = []

        for frequency in range(len(nums), 0, -1):
            for number in buckets[frequency]:
                result.append(number)
                if len(result) == k:
                    return result

        return result
