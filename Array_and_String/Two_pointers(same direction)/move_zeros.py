# Problem: 283. Move Zeroes
# LeetCode: https://leetcode.com/problems/move-zeroes/
# Author: srinivas
# Date: 2025-11-12
# Language: Python3

"""
Given an integer array nums, move all 0's to the end of it while maintaining 
the relative order of the non-zero elements.

You must do this in-place without making a copy of the array.

Example 1:
Input: nums = [0,1,0,3,12]
Output: [1,3,12,0,0]

Example 2:
Input: nums = [0]
Output: [0]

Constraints:
- 1 <= nums.length <= 10^4
- -2^31 <= nums[i] <= 2^31 - 1

Follow-up: Could you minimize the total number of operations done?
"""


class Solution:
    def moveZeroes(self, nums):
        """
        Moves all zeros in the array 'nums' to the end while maintaining 
        the order of non-zero elements. The operation is performed in-place.
        """
        # 🧠 TODO: Implement logic here

        if not nums:
            return []

        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != 0:
                nums[slow], nums[fast] = nums[fast], nums[slow]
                slow = slow+1

        return nums


# --------- Local Test Harness ---------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        # ✅ Basic case
        {
            "input": [0, 1, 0, 3, 12],
            "expected": [1, 3, 12, 0, 0],
        },
        # ✅ Single zero
        {
            "input": [0],
            "expected": [0],
        },
        # ✅ No zeros
        {
            "input": [1, 2, 3, 4],
            "expected": [1, 2, 3, 4],
        },
        # ✅ All zeros
        {
            "input": [0, 0, 0, 0],
            "expected": [0, 0, 0, 0],
        },
        # ✅ Zeros at the end (should remain unchanged)
        {
            "input": [1, 2, 3, 0, 0],
            "expected": [1, 2, 3, 0, 0],
        },
        # ✅ Zeros at the beginning
        {
            "input": [0, 0, 1, 2, 3],
            "expected": [1, 2, 3, 0, 0],
        },
        # ✅ Mixed pattern
        {
            "input": [4, 0, 5, 0, 0, 6, 7],
            "expected": [4, 5, 6, 7, 0, 0, 0],
        },
        # ✅ Large case
        {
            "input": [0, 1, 0, 2, 0, 3, 0, 4],
            "expected": [1, 2, 3, 4, 0, 0, 0, 0],
        },
    ]

    for i, t in enumerate(tests, 1):
        nums_copy = t["input"].copy()
        sol.moveZeroes(nums_copy)
        print(
            f"Test {i}: input={t['input']} => result={nums_copy}, expected={t['expected']}, "
            f"{'✅ PASS' if nums_copy == t['expected'] else '❌ FAIL'}"
        )
