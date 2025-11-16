# problem: 643. Maximum Average Subarray I
# leetcode: https://leetcode.com/problems/maximum-average-subarray-i/description/
# author: srinivas
# date: 2025-11-16
# language: python3


from typing import List


class Solution:
    def findMaxAverage(self, nums: List[int], k: int) -> float:
        """
        Sliding window solution.
        Returns the maximum average of any contiguous subarray of length k.
        """
        curr_sum = sum(nums[:k])
        max_sum = curr_sum
        for i in range(k, len(nums)):
            curr_sum += nums[i] - nums[i-k]
            max_sum = max(max_sum, curr_sum)

        return max_sum/k
# -------------------------
# Test Cases
# -------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (nums, k, expected_output)
        ([1, 12, -5, -6, 50, 3], 4, 12.75),
        ([5], 1, 5.0),
        ([0, 0, 0, 0], 2, 0.0),
        ([1, 2, 3, 4, 5], 1, 5.0),
        ([1, 2, 3, 4, 5], 5, 3.0),
        ([-1, -2, -3, -4], 2, -1.5),
        ([-5, -3, -1], 3, -3.0),
        ([7, 4, 5, 8, 8, 3, 9, 8, 7, 6], 7, 7.0),
        ([9, 7, 3, 5, 6, 2, 0, 8, 1], 3, 6.0),
        ([4, 2, 1, 3, 6, 2, 8], 2, 5.0),
        ([100, 50, 100, 50], 2, 75.0),
        ([1, 1, 1, 1, 1, 50], 3, 17.6666666667),
    ]

    for i, (nums, k, expected) in enumerate(tests, 1):
        result = sol.findMaxAverage(nums, k)
        print(f"Test {i}:")
        print(f" nums:     {nums}")
        print(f" k:        {k}")
        print(f" Output:   {result}")
        print(f" Expected: {expected}")
        print(" Pass:", abs(result - expected) < 1e-5)
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
