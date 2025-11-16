# problem: 167. Two Sum II - input array is sorted
# leetcode: https://leetcode.com/problems/two-sum-ii-input-array-is-sorted/description/
# author: srinivas
# date: 2025-11-16
# language: python3

from typing import List


class Solution:
    def twoSum(self, numbers: List[int], target: int) -> List[int]:
        """
        Two-pointer approach.
        Returns 1-based indices of the two numbers that add up to target.
        """
        left = 0
        right = len(numbers)-1

        while (left < right):
            sum = numbers[left] + numbers[right]
            if target == sum:
                return [left+1, right+1]
            elif sum < target:
                left += 1
            else:
                right -= 1

        return []
# -------------------------
# Test Cases
# -------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (numbers, target, expected_answer)
        ([2, 7, 11, 15], 9, [1, 2]),
        ([2, 3, 4], 6, [1, 3]),
        ([-1, 0], -1, [1, 2]),
        ([1, 3, 4, 5, 7, 11], 9, [2, 4]),
        ([1, 2, 3, 4, 4, 9, 56, 90], 8, [4, 5]),
        ([1, 2], 3, [1, 2]),
    ]

    for i, (nums, target, expected) in enumerate(tests, 1):
        result = sol.twoSum(nums, target)
        print(f"Test {i}:")
        print(f" Input: numbers={nums}, target={target}")
        print(f" Output: {result}")
        print(f" Expected: {expected}")
        print(" Pass:", result == expected)
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
