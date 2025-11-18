# Problem: 268. Missing number
# LeetCode: https://leetcode.com/problems/missing-number/description/
# Author: srinivas
# Date: 2025-11-18
# Language: Python3


class Solution:
    def missingNumber(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """

        # cyclic sort
        """
        for i in range(len(nums)):
            corrent_index = nums[i]

            if nums[i] < len(nums) and nums[i] != nums[corrent_index]:
                nums[i], nums[corrent_index] = nums[corrent_index], nums[i]

        for i in range(len(nums)):
            if nums[i] != i:
                return i

        return len(nums)
        """

        n = len(nums)
        expected_sum = n * (n+1)//2
        return expected_sum - sum(nums)
# --------------------------
# Test Cases
# --------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (input, expected_output)
        ([3, 0, 1], 2),
        ([0, 1], 2),
        ([9, 6, 4, 2, 3, 5, 7, 0, 1], 8),
        ([0], 1),
        ([1], 0),
        ([0, 2], 1),
        ([1, 2], 0),
        ([2, 3, 4, 5, 0], 1),
        ([], 0),                 # empty means missing 0
        (list(range(1, 101)), 0),  # missing 0
        (list(range(0, 100)), 100),  # missing last number
    ]

    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.missingNumber(nums)
        print(f"Test {i}: nums={nums}")
        print(f"  Expected: {expected}, Got: {result}")
        print("  PASS" if result == expected else "  FAIL")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
