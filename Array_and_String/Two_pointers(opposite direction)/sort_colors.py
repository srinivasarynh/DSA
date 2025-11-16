# problem: 75. Sort Colors
# leetcode: https://leetcode.com/problems/sort-colors/description/
# author: srinivas
# date: 2025-11-16
# language: python3


from typing import List


class Solution:
    def sortColors(self, nums: List[int]) -> None:
        """
        Sorts the list containing 0s, 1s, and 2s in-place
        using the Dutch National Flag algorithm.
        """
        left = 0
        right = len(nums)-1
        mid = 0

        while mid <= right:
            if nums[mid] == 0:
                nums[left], nums[mid] = nums[mid], nums[left]
                left += 1
                mid += 1
            elif nums[mid] == 1:
                mid += 1
            else:
                nums[right], nums[mid] = nums[mid], nums[right]
                right -= 1

# -------------------------
# Test Cases
# -------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (input_list, expected_output)
        ([2, 0, 2, 1, 1, 0], [0, 0, 1, 1, 2, 2]),
        ([2, 0, 1], [0, 1, 2]),
        ([0], [0]),
        ([1], [1]),
        ([2], [2]),
        ([], []),
        ([1, 2, 0, 1, 2, 0], [0, 0, 1, 1, 2, 2]),
        ([0, 0, 0], [0, 0, 0]),
        ([1, 1, 1], [1, 1, 1]),
        ([2, 2, 2], [2, 2, 2]),
        ([0, 2, 1], [0, 1, 2]),
        ([2, 1, 0], [0, 1, 2]),
        ([1, 0, 2, 1, 0, 2], [0, 0, 1, 1, 2, 2]),
        ([0, 1, 2, 0, 1, 2, 0, 1, 2], [0, 0, 0, 1, 1, 1, 2, 2, 2]),
        ([2, 1, 2, 1, 0], [0, 1, 1, 2, 2]),
    ]

    for i, (nums, expected) in enumerate(tests, 1):
        arr = nums[:]  # copy so original test case stays unchanged
        sol.sortColors(arr)
        print(f"Test {i}:")
        print(f" Input:    {nums}")
        print(f" Output:   {arr}")
        print(f" Expected: {expected}")
        print(" Pass:", arr == expected)
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
