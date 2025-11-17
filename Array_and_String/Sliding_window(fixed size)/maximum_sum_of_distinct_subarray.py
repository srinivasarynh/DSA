# problem: 2461. Maximum Sum of Distinct Subarrays with Length K
# leetcode: https://leetcode.com/problems/maximum-sum-of-distinct-subarrays-with-length-k/description/
# author: srinivas
# date: 2025-11-16
# language: python3


from typing import List
from collections import defaultdict


class Solution:
    def maximumSubarraySum(self, nums: List[int], k: int) -> int:
        """
        Sliding-window with frequency map.
        Window must have size k AND contain all distinct values to be considered.
        """
        freq = defaultdict(int)
        window_sum = 0
        max_sum = 0
        left = 0

        for right in range(len(nums)):
            freq[nums[right]] += 1
            window_sum += nums[right]

            if right - left + 1 > k:
                freq[nums[left]] -= 1
                if freq[nums[left]] == 0:
                    del freq[nums[left]]
                window_sum -= nums[left]
                left += 1

            if right-left+1 == k:
                if len(freq) == k:
                    max_sum = max(window_sum, max_sum)

        return max_sum
# -------------------------
# Test Cases
# -------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (nums, k, expected_output)
        ([1, 5, 4, 2, 9, 9, 9], 3, 15),
        ([4, 4, 4], 3, 0),
        ([1, 2, 3, 4, 5], 3, 12),
        ([5, 2, 3, 5, 7, 8], 3, 20),
        ([9, 9, 9, 9], 1, 9),
        ([9, 9, 9, 9], 2, 0),
        ([1], 1, 1),
        ([100, 200, 300], 2, 500),
        ([1, 2, 1, 3, 2, 3, 4], 3, 10),
        ([7, 3, 5, 3, 1, 3, 9], 3, 17),
        ([2, 2, 2, 2, 2], 1, 2),
        ([2, 2, 2, 2, 2], 2, 0),
        ([1, 2, 3], 4, 0),                        # window > length
        ([3, 1, 2, 2, 4, 5, 2, 1], 3, 11),
        ([1, 2, 3, 2, 5], 3, 10),
        ([10, 20, 10, 30, 40], 2, 70),
    ]

    for i, (nums, k, expected) in enumerate(tests, 1):
        result = sol.maximumSubarraySum(nums, k)
        print(f"Test {i}:")
        print(f" nums:     {nums}")
        print(f" k:        {k}")
        print(f" Output:   {result}")
        print(f" Expected: {expected}")
        print(" Pass:", result == expected)
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
