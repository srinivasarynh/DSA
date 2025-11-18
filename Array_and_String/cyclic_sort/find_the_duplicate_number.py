# Problem: 287. Find the Duplicate Number
# LeetCode: https://leetcode.com/problems/find-the-duplicate-number/description/
# Author: srinivas
# Date: 2025-11-18
# Language: Python3


class Solution:
    def findDuplicate(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        n = len(nums)
        i = 0

        while (i < n):
            correct_index = nums[i]-1
            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        for i in range(len(nums)):
            if nums[i] != i+1:
                return nums[i]

        return n
# --------------------------
# Test Cases
# --------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (input, expected_output)
        ([1, 3, 4, 2, 2], 2),
        ([3, 1, 3, 4, 2], 3),
        ([1, 1], 1),
        ([1, 1, 2], 1),
        ([2, 2, 2, 2, 2], 2),
        ([1, 4, 6, 2, 3, 5, 6], 6),
        ([5, 4, 3, 2, 1, 3], 3),
        ([2, 1, 4, 3, 2], 2),
        ([9, 8, 7, 6, 5, 4, 3, 2, 1, 9], 9),
        ([4, 3, 1, 4, 2], 4),
    ]

    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.findDuplicate(nums)
        print(f"Test {i}: nums={nums}")
        print(f"  Expected: {expected}, Got: {result}")
        print("  PASS" if result == expected else "  FAIL")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
