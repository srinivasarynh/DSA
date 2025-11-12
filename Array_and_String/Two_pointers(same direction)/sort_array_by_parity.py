# Problem: 905. Sort Array By Parity
# LeetCode: https://leetcode.com/problems/sort-array-by-parity/
# Author: srinivas
# Date: 2025-11-12
# Language: Python3

"""
Given an integer array nums, move all the even integers to the beginning of 
the array followed by all the odd integers.

Return any array that satisfies this condition.

Example 1:
Input: nums = [3,1,2,4]
Output: [2,4,3,1]
Explanation: The outputs [4,2,3,1], [2,4,1,3], and [4,2,1,3] would also be accepted.

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
- 1 <= nums.length <= 5000
- 0 <= nums[i] <= 5000
"""


class Solution:
    def sortArrayByParity(self, nums):
        """
        Rearranges the array so that all even numbers come before odd numbers.
        Returns the modified list.
        """
        # 🧠 TODO: Implement logic here
        if not nums:
            return []

        slow = 0
        for fast in range(len(nums)):
            if nums[fast] % 2 == 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow += 1

        return nums


# --------- Local Test Harness ---------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        # ✅ Basic example
        # or any even-odd partition
        {"input": [3, 1, 2, 4], "expected": [2, 4, 3, 1]},
        # ✅ Single element (even)
        {"input": [0], "expected": [0]},
        # ✅ Single element (odd)
        {"input": [7], "expected": [7]},
        # ✅ All even
        {"input": [2, 4, 6, 8], "expected": [2, 4, 6, 8]},
        # ✅ All odd
        {"input": [1, 3, 5, 7], "expected": [1, 3, 5, 7]},
        # ✅ Alternating even and odd
        {"input": [1, 2, 3, 4, 5, 6], "expected": [2, 4, 6, 1, 3, 5]},
        # ✅ Random mix
        {"input": [9, 8, 3, 12, 5, 10], "expected": [8, 12, 10, 9, 3, 5]},
        # ✅ Large case (edge check)
        {"input": [i for i in range(10)], "expected": [
            0, 2, 4, 6, 8, 1, 3, 5, 7, 9]},
    ]

    def is_valid_parity_sort(result):
        """Helper to validate even elements come before odd elements."""
        seen_odd = False
        for num in result:
            if num % 2 == 0:
                if seen_odd:
                    return False
            else:
                seen_odd = True
        return True

    for i, t in enumerate(tests, 1):
        result = sol.sortArrayByParity(t["input"].copy())
        valid = is_valid_parity_sort(result)
        print(
            f"Test {i}: input={t['input']} => result={result}, "
            f"{'✅ PASS' if valid else '❌ FAIL'}"
        )
