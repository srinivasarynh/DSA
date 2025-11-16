# problem: 219. Contains Duplicate II
# leetcode: https://leetcode.com/problems/contains-duplicate-ii/description/
# author: srinivas
# date: 2025-11-16
# language: python3


from typing import List


class Solution:
    def containsNearbyDuplicate(self, nums: List[int], k: int) -> bool:
        """
        Returns True if there exist two distinct indices i and j
        such that nums[i] == nums[j] and abs(i - j) <= k.

        Uses a sliding window with a hash set.
        """
        window = set()
        for i, num in enumerate(nums):
            if num in window:
                return True
            window.add(num)

            if len(window) > k:
                window.remove(nums[i-k])

        return False

# -------------------------
# Test Cases
# -------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (nums, k, expected_output)
        ([1, 2, 3, 1], 3, True),
        ([1, 0, 1, 1], 1, True),
        ([1, 2, 3, 1, 2, 3], 2, False),
        ([99, 99], 2, True),
        ([1, 2, 3, 4, 5], 1, False),
        ([1, 2, 3, 4, 1], 3, True),
        ([1, 2, 3, 4, 1], 2, False),
        ([], 3, False),
        ([1], 1, False),
        ([2, 2], 0, False),
        ([2, 2], 1, True),
        ([1, 2, 1, 3, 1, 2, 1], 3, True),
        ([1, 2, 1, 3, 1, 2, 1], 1, False),
        ([10, 20, 30, 10], 3, True),
        ([-1, -1], 1, True),
        ([-1, -1, 2, 3], 2, True),
        ([-1, 2, 3, 4], 0, False),
        ([5, 5, 5, 5], 2, True),
    ]

    for i, (nums, k, expected) in enumerate(tests, 1):
        result = sol.containsNearbyDuplicate(nums, k)
        print(f"Test {i}:")
        print(f" nums:     {nums}")
        print(f" k:        {k}")
        print(f" Output:   {result}")
        print(f" Expected: {expected}")
        print(" Pass:", result == expected)
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
