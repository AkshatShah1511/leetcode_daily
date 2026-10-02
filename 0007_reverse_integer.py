# LeetCode 7: Reverse Integer
# https://leetcode.com/problems/reverse-integer/
# Added: 2026-10-02 (Asia/Calcutta)
# Selection: Fallback; today's official daily challenge could not be verified.
#
# Approach:
# Remove digits from the absolute value from right to left and append each
# digit to the reversed number. Before appending, check whether multiplying
# by 10 and adding the digit would exceed the allowed 32-bit magnitude.
# Apply the original sign only after every digit has been processed.
#
# Correctness:
# After each iteration, reversed_value contains exactly the digits already
# removed from x, in reverse order. Appending the next last digit preserves
# this invariant. When no digits remain, reversed_value is therefore the
# complete digit reversal. The pre-update bound check returns 0 precisely
# when the next value would exceed the signed 32-bit range; otherwise applying
# the original sign produces the required valid result.
#
# Complexity: O(log10(|x| + 1)) time and O(1) auxiliary space.

class Solution:
    def reverse(self, x: int) -> int:
        sign = -1 if x < 0 else 1
        remaining = abs(x)

        # A negative 32-bit integer may have magnitude 2^31, while the
        # largest positive value has magnitude 2^31 - 1.
        limit = 2**31 if sign < 0 else 2**31 - 1
        reversed_value = 0

        while remaining:
            remaining, digit = divmod(remaining, 10)

            # This form checks overflow before performing the update.
            if reversed_value > (limit - digit) // 10:
                return 0

            reversed_value = reversed_value * 10 + digit

        return sign * reversed_value
