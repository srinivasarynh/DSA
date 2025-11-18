# Problem: 442. Find all duplicates in an array
# LeetCode: https://leetcode.com/problems/find-all-duplicates-in-an-array/description/
# Author: srinivas
# Date: 2025-11-18
# Language: Python3


# LeetCode 442: Find All Duplicates in an Array
# Python3 template with test cases

class Solution:
    def findDuplicates(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        i = 0
        n = len(nums)
        missing = []

        while (i < n):
            correct_index = nums[i]-1
            if nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i+1:
                missing.append(nums[i])

        return missing
# --------------------------
# Test Cases
# --------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (input, expected_output)
        ([4, 3, 2, 7, 8, 2, 3, 1], [2, 3]),
        ([1, 1, 2], [1]),
        ([1, 2, 3], []),
        ([2, 2], [2]),
        ([3, 3, 3], [3, 3]),      # multiple repeats
        ([1], []),
        ([1, 1], [1]),
        ([2, 1, 2, 3, 3, 4], [2, 3]),
        ([5, 4, 3, 2, 1], []),
        ([10, 2, 5, 10, 9, 1, 1, 4, 3, 7], [10, 1]),
    ]

    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.findDuplicates(nums.copy())
        print(f"Test {i}: nums={nums}")
        print(f"  Expected: {expected}, Got: {result}")
        print("  PASS" if sorted(result) == sorted(expected) else "  FAIL")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
