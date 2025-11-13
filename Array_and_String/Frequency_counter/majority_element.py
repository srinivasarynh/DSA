# Problem: 169. Majority Element
# LeetCode: https://leetcode.com/problems/majority-element/
# Author: srinivas
# Date: 2025-11-13
# Language: Python3


"""
LeetCode Problem 169: Majority Element
Difficulty: Easy
Pattern: Frequency Counter (Hash Map)

🧩 Problem Statement:
Given an array `nums` of size n, return the element that appears more than ⌊n / 2⌋ times.
You may assume that the majority element always exists in the array.

Constraints:
- n == len(nums)
- 1 <= n <= 5 * 10^4
- -10^9 <= nums[i] <= 10^9
"""

from typing import List
from collections import Counter


class Solution:
    def majorityElement(self, nums: List[int]) -> int:
        """
        Count occurrences of each number using a hash map (Counter).
        Return the element whose frequency is greater than n // 2.
        """

        freq = Counter(nums)
        for num, count in freq.items():
            if count > (len(nums)//2):
                return num


# ----------------------------
# ✅ Test Cases
# ----------------------------


def run_tests():
    sol = Solution()

    test_cases = [
        # Example cases
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),

        # Edge cases
        ([1], 1),                      # single element
        ([5, 5, 5, 5], 5),             # all same element
        ([1, 1, 2], 1),                # 1 occurs twice > n/2 = 1
        ([6, 7, 7, 7, 6, 7, 7], 7),    # clear majority
        ([0, 0, 0, 1, 1], 0),          # majority 0
        ([-1, -1, -1, 0, 1], -1),      # negative numbers
        # large case where 9999 dominates
        (list(range(10000)) + [9999]*10000, 9999),
    ]

    for idx, (nums, expected) in enumerate(test_cases, 1):
        result = sol.majorityElement(nums)
        assert result == expected, f"❌ Test {idx} failed: expected {expected}, got {result}"
        print(f"✅ Test {idx} passed")


if __name__ == "__main__":
    run_tests()
