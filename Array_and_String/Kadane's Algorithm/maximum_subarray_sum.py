# problem: 53. Maxumum Subarray sum
# leetcode: https://leetcode.com/problems/maximum-subarray/description/
# author: srinivas
# date: 2025-11-17
# language: python3


from typing import List


class Solution:
    def maxSubArray(self, nums: List[int]) -> int:
        # TODO: Replace with your own implementation
        # Reference: Kadane's algorithm

        curr_sum = nums[0]
        max_sum = nums[0]

        for num in nums[1:]:
            curr_sum = max(num, curr_sum+num)
            max_sum = max(max_sum, curr_sum)

        return max_sum

# ---------------------------------------------------------
# Test Harness
# ---------------------------------------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (nums, expected)

        # Basic examples
        ([-2, 1, -3, 4, -1, 2, 1, -5, 4], 6),     # [4,-1,2,1]
        ([1], 1),
        ([5, 4, -1, 7, 8], 23),               # whole array

        # All negative values
        ([-1, -2, -3, -4], -1),
        ([-10], -10),

        # All positive values
        ([1, 2, 3, 4], 10),
        ([100, 200, 300], 600),

        # Mix of small sequences
        ([2, -1, 2], 3),
        ([8, -19, 5, -4, 20], 21),            # [5,-4,20]

        # Alternating positive/negative
        ([1, -1, 1, -1, 1, -1, 5], 6),          # last segments
        ([4, -1, 2, 1], 6),

        # Zeros in between
        ([0, 0, 0], 0),
        ([0, -1, 2, 3, 0, 1], 6),

        # Long uniform patterns
        ([3]*10, 30),
        ([-3]*10, -3),

        # Tricky sequences
        ([-2, -1], -1),
        ([-2, 1], 1),
        ([1, -2, 3, 5, -1, 2], 9),        # [3,5,-1,2]

        # Mixed with big swings
        ([100, -90, 200, -300, 400], 400),
        ([100, -50, 100, -50, 100], 200),
    ]

    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.maxSubArray(nums)
        print(f"Test {i}: ", end="")
        if result == expected:
            print(f"PASS (result={result})")
        else:
            print(f"FAIL (result={result}, expected={expected})")


if __name__ == "__main__":
    run_tests()
