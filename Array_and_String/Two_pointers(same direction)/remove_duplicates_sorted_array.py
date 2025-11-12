# Problem: 26. Remove Duplicates from Sorted Array
# LeetCode: https://leetcode.com/problems/remove-duplicates-from-sorted-array/
# Author: srinivas
# Date: 2025-11-12
# Language: Python3

"""
Given an integer array nums sorted in non-decreasing order, remove the duplicates in-place 
such that each unique element appears only once. The relative order of the elements should 
be kept the same.

After removing duplicates, return the number of unique elements k.

The first k elements of nums should contain the unique numbers in sorted order. 
The remaining elements beyond index k - 1 can be ignored.

Example 1:
Input: nums = [1,1,2]
Output: 2, nums = [1,2,_]

Example 2:
Input: nums = [0,0,1,1,1,2,2,3,3,4]
Output: 5, nums = [0,1,2,3,4,_,_,_,_,_]

Constraints:
- 1 <= nums.length <= 3 * 10^4
- -100 <= nums[i] <= 100
- nums is sorted in non-decreasing order.
"""


class Solution:
    def removeDuplicates(self, nums):
        """
        Removes duplicates in-place from a sorted array.
        Returns:
            int: The number of unique elements (k).
        The first k elements of nums will contain the unique values.
        """
        # 🧠 TODO: Implement logic here
        if not nums:
            return 0

        slow = 0
        for fast in range(1, len(nums)):
            if nums[slow] != nums[fast]:
                slow = slow+1
                nums[slow] = nums[fast]

        return slow+1


# --------- Local Test Harness ---------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        # ✅ Basic test (from problem statement)
        {
            "input": [1, 1, 2],
            "expected_k": 2,
            "expected_nums": [1, 2],
        },
        # ✅ Larger input with multiple duplicates
        {
            "input": [0, 0, 1, 1, 1, 2, 2, 3, 3, 4],
            "expected_k": 5,
            "expected_nums": [0, 1, 2, 3, 4],
        },
        # ✅ All unique elements (no change)
        {
            "input": [1, 2, 3, 4, 5],
            "expected_k": 5,
            "expected_nums": [1, 2, 3, 4, 5],
        },
        # ✅ All duplicates (only one unique element)
        {
            "input": [7, 7, 7, 7],
            "expected_k": 1,
            "expected_nums": [7],
        },
        # ✅ Single element (edge case)
        {
            "input": [10],
            "expected_k": 1,
            "expected_nums": [10],
        },
        # ✅ Negative numbers & duplicates
        {
            "input": [-3, -3, -2, -1, -1, 0, 0, 1],
            "expected_k": 5,
            "expected_nums": [-3, -2, -1, 0, 1],
        },
    ]

    for i, t in enumerate(tests, 1):
        nums_copy = t["input"].copy()
        result_k = sol.removeDuplicates(nums_copy)
        result_nums = nums_copy[:result_k]

        print(
            f"Test {i}: input={t['input']}, expected_k={t['expected_k']}, "
            f"result_k={result_k}, expected_nums={t['expected_nums']}, result_nums={result_nums}, "
            f"{'✅ PASS' if (result_k == t['expected_k'] and result_nums == t['expected_nums']) else '❌ FAIL'}"
        )
