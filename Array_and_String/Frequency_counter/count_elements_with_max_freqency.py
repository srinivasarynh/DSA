# Problem: 3005. Count Elements With maximum frequency
# LeetCode: https://leetcode.com/problems/count-elements-with-maximum-frequency/description/?utm_source=chatgpt.com
# Author: srinivas
# Date: 2025-11-13
# Language: Python3

"""
Problem: Count Elements With Maximum Frequency
Difficulty: Easy
Pattern: Frequency Counter (Hash Map)

🧩 Problem Statement:
You are given an integer array `nums`.
Return the total number of elements that appear as frequently as the most frequent element.

Example:
Input: nums = [1,2,2,3,1,4]
Output: 4
Explanation:
- 1 appears twice, 2 appears twice, 3 and 4 appear once.
- The maximum frequency is 2.
- Numbers appearing with frequency 2 are 1 and 2 (2 + 2 = 4 elements).

Constraints:
- 1 <= len(nums) <= 100
- 1 <= nums[i] <= 100
"""

from typing import List
from collections import Counter


class Solution:
    def maxFrequencyElements(self, nums: List[int]) -> int:
        """
        Count how many elements appear as frequently as the most frequent element.
        """

        # Brute force
        """
        freq = dict()
        for element in nums:
            if element not in freq:
                freq[element] = 1

            freq[element] += 1
        """
        freq = Counter(nums)
        max_freq = max(freq.values())
        total_count = sum(count for count in freq.values()
                          if count == max_freq)
        return total_count

# ----------------------------
# ✅ Test Cases
# ----------------------------


def run_tests():
    sol = Solution()

    test_cases = [
        # Example cases
        ([1, 2, 2, 3, 1, 4], 4),     # max freq = 2, elements 1 and 2 → 2+2=4
        ([1, 2, 3, 4, 5], 5),       # all unique → max freq = 1 → all 5 counted
        ([1, 1, 1, 1], 4),         # single number → max freq = 4 → total = 4
        ([1, 2, 2, 3, 3, 3], 3),     # max freq = 3 (num=3) → total = 3

        # Edge cases
        ([7], 1),               # single element → freq=1
        ([5, 5, 6, 6, 7, 7], 6),     # all have freq=2 → total = 6
        ([1, 2, 3, 3, 2, 2], 3),     # max freq = 3 for 2
        # max freq=3 for 30,40 → 3+3=6
        ([10, 10, 20, 30, 30, 30, 40, 40, 40], 6),
        ([100]*100, 100),       # all same element → freq=100
        # uniform distribution, all freq=10 → 10*10=100
        ([i % 10 for i in range(100)], 100),
    ]

    for idx, (nums, expected) in enumerate(test_cases, 1):
        result = sol.maxFrequencyElements(nums)
        assert result == expected, f"❌ Test {idx} failed: expected {expected}, got {result}"
        print(f"✅ Test {idx} passed")


if __name__ == "__main__":
    run_tests()
