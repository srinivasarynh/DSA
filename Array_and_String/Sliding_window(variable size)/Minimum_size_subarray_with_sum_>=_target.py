# problem: 209. Minimum size subarray sum
# leetcode: https://leetcode.com/problems/minimum-size-subarray-sum/description/
# author: srinivas
# date: 2025-11-17
# language: python3


from typing import List


class Solution:
    def minSubArrayLen(self, target: int, nums: List[int]) -> int:
        # TODO: replace with your own implementation
        # Reference implementation provided for convenience.

        left = 0
        total = 0
        min_len = float('inf')

        for right in range(len(nums)):
            total += nums[right]

            while total >= target:
                min_len = min(min_len, right-left+1)
                total -= nums[left]
                left += 1

        return 0 if min_len == float('inf') else min_len
# ---------------------------------------------------------
# Test Harness
# ---------------------------------------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (target, nums, expected)

        # Provided examples
        (7, [2, 3, 1, 2, 4, 3], 2),                 # subarray [4,3]
        (4, [1, 4, 4], 1),                       # [4]
        (11, [1, 1, 1, 1, 1, 1, 1, 1], 0),            # no valid subarray

        # Edge cases
        (5, [], 0),
        (1, [1], 1),
        (2, [1], 0),
        (3, [3], 1),

        # Increasing sequences
        (15, [1, 2, 3, 4, 5], 2),                  # [5,4] or [4,5]

        # Multiple valid windows
        (7, [1, 2, 3, 4, 5], 2),                   # [3,4], [4,3], etc.

        # Large numbers for small windows
        (100, [50, 50, 1, 1, 1], 2),

        # Exact match cases
        (6, [1, 2, 3], 3),
        (6, [3, 3, 3], 2),

        # Random-style cases
        (8, [3, 1, 2, 1, 1, 1, 5], 2),               # [3,5]
        (9, [2, 3, 1, 2, 1, 1, 6], 2),               # [3,6]

        # Sliding window tightening scenarios
        (10, [2, 3, 1, 2, 4, 3], 3),                # [3,1,2,4]
    ]

    for i, (target, nums, expected) in enumerate(tests, 1):
        result = sol.minSubArrayLen(target, nums)
        print(f"Test {i}: ", end="")
        if result == expected:
            print(f"PASS (result={result})")
        else:
            print(f"FAIL (result={result}, expected={expected})")


if __name__ == "__main__":
    run_tests()
