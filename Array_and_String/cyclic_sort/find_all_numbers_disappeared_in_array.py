# Problem: 448. find all numbers disappeared in an array
# LeetCode: https://leetcode.com/problems/find-all-numbers-disappeared-in-an-array/description/
# Author: srinivas
# Date: 2025-11-18
# Language: Python3


class Solution:
    def findDisappearedNumbers(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        i = 0
        missing = []

        while (i < n):
            correct_index = nums[i]-1

            if nums[i] < n-1 and nums[i] != nums[correct_index]:
                nums[i], nums[correct_index] = nums[correct_index], nums[i]
            else:
                i += 1

        for i in range(n):
            if nums[i] != i+1:
                missing.append(i+1)

        return missing

# --------------------------
# Test Cases
# --------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (input, expected_output)
        ([4, 3, 2, 7, 8, 2, 3, 1], [5, 6]),
        ([1, 1], [2]),
        ([2, 2], [1]),
        ([1], []),
        ([2], [1]),
        ([1, 2, 3, 4, 5], []),
        ([5, 4, 3, 2, 1], []),
        ([1, 1, 2, 2], [3, 4]),
        ([3, 3, 3], [1, 2]),
        ([4, 3, 2, 7, 7, 2, 3, 1], [5, 6]),
        ([], []),  # edge case, though LC won't give empty
    ]

    for i, (nums, expected) in enumerate(tests, 1):
        # copy nums so each test uses fresh input
        result = sol.findDisappearedNumbers(nums.copy())
        print(f"Test {i}: nums={nums}")
        print(f"  Expected: {expected}, Got: {result}")
        print("  PASS" if sorted(result) == sorted(expected) else "  FAIL")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
