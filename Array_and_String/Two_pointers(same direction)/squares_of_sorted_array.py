
# Problem: 977. Squares of a Sorted Array
# LeetCode: https://leetcode.com/problems/squares-of-a-sorted-array/
# Author: srinivas
# Date: 2025-11-12
# Language: Python3

"""
Given an integer array nums sorted in non-decreasing order,
return an array of the squares of each number sorted in non-decreasing order.

Example 1:
Input: nums = [-4, -1, 0, 3, 10]
Output: [0, 1, 9, 16, 100]
Explanation:
After squaring, the array becomes [16, 1, 0, 9, 100].
After sorting, it becomes [0, 1, 9, 16, 100].

Example 2:
Input: nums = [-7, -3, 2, 3, 11]
Output: [4, 9, 9, 49, 121]

Constraints:
- 1 <= nums.length <= 10^4
- -10^4 <= nums[i] <= 10^4
- nums is sorted in non-decreasing order.
"""


class Solution:
    def sortedSquares(self, nums):
        """
        Given a sorted array, return an array of the squares of each number,
        sorted in non-decreasing order.
        """
        # 🧠 TODO: Implement logic here
        # return sorted(x * x for x in nums)

        result = [0] * len(nums)
        left = 0
        right = len(nums)-1
        residx = len(nums)-1

        while (left <= right):
            leftsqr = nums[left] * nums[left]
            rightsqr = nums[right] * nums[right]
            if leftsqr > rightsqr:
                result[residx] = leftsqr
                left += 1
                residx -= 1
            else:
                result[residx] = rightsqr
                right -= 1
                residx -= 1

        return result


# --------- Local Test Harness ---------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        # ✅ Example cases
        {"input": [-4, -1, 0, 3, 10], "expected": [0, 1, 9, 16, 100]},
        {"input": [-7, -3, 2, 3, 11], "expected": [4, 9, 9, 49, 121]},
        # ✅ All non-negative numbers
        {"input": [0, 1, 2, 3, 4], "expected": [0, 1, 4, 9, 16]},
        # ✅ All negative numbers
        {"input": [-5, -4, -3, -2, -1], "expected": [1, 4, 9, 16, 25]},
        # ✅ Mix of large and small values
        {"input": [-10, -5, 0, 5, 10], "expected": [0, 25, 25, 100, 100]},
        # ✅ Single element (positive)
        {"input": [3], "expected": [9]},
        # ✅ Single element (negative)
        {"input": [-3], "expected": [9]},
        # ✅ Two elements
        {"input": [-1, 2], "expected": [1, 4]},
    ]

    for i, t in enumerate(tests, 1):
        result = sol.sortedSquares(t["input"].copy())
        print(
            f"Test {i}: input={t['input']} => result={result}, expected={t['expected']}, "
            f"{'✅ PASS' if result == t['expected'] else '❌ FAIL'}"
        )
