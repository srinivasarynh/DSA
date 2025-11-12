# Problem: 27. Remove Element
# LeetCode: https://leetcode.com/problems/remove-element/
# Author: srinivas
# Date: 2025-11-12
# Language: Python3

"""
Given an integer array nums and an integer val, remove all occurrences of val in-place.
The order of the elements may be changed. Then return the number of elements in nums 
which are not equal to val.

Consider the number of elements in nums which are not equal to val be k.
To get accepted, you need to:
  - Modify the array nums so that the first k elements contain only elements != val.
  - Return k.
  - The remaining elements beyond k do not matter.

Example 1:
Input: nums = [3,2,2,3], val = 3
Output: 2, nums = [2,2,_,_]

Example 2:
Input: nums = [0,1,2,2,3,0,4,2], val = 2
Output: 5, nums = [0,1,4,0,3,_,_,_]

Constraints:
- 0 <= nums.length <= 100
- 0 <= nums[i] <= 50
- 0 <= val <= 100
"""


class Solution:
    def removeElement(self, nums, val):
        """
        Removes all occurrences of `val` in-place from `nums`.
        Returns:
            int: Number of elements not equal to `val`.
        The first k elements of nums will contain those valid elements.
        """
        # 🧠 TODO: Implement logic here
        if not nums:
            return 0

        slow = 0
        for fast in range(len(nums)):
            if nums[fast] != val:
                nums[slow] = nums[fast]
                slow = slow+1

        return slow


# --------- Local Test Harness ---------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        # ✅ Basic test (from problem statement)
        {
            "input": {"nums": [3, 2, 2, 3], "val": 3},
            "expected_k": 2,
            "expected_nums": [2, 2],
        },
        # ✅ Multiple occurrences in different positions
        {
            "input": {"nums": [0, 1, 2, 2, 3, 0, 4, 2], "val": 2},
            "expected_k": 5,
            # order can vary, check by sorting
            "expected_nums": [0, 1, 3, 0, 4],
        },
        # ✅ No elements equal to val
        {
            "input": {"nums": [1, 2, 3, 4], "val": 5},
            "expected_k": 4,
            "expected_nums": [1, 2, 3, 4],
        },
        # ✅ All elements equal to val
        {
            "input": {"nums": [2, 2, 2, 2], "val": 2},
            "expected_k": 0,
            "expected_nums": [],
        },
        # ✅ Mixed order elements
        {
            "input": {"nums": [4, 1, 4, 3, 4, 5], "val": 4},
            "expected_k": 3,
            "expected_nums": [1, 3, 5],
        },
        # ✅ Empty array
        {
            "input": {"nums": [], "val": 0},
            "expected_k": 0,
            "expected_nums": [],
        },
        # ✅ Edge values (val = 0)
        {
            "input": {"nums": [0, 0, 1, 2, 3], "val": 0},
            "expected_k": 3,
            "expected_nums": [1, 2, 3],
        },
    ]

    for i, t in enumerate(tests, 1):
        nums_copy = t["input"]["nums"].copy()
        result_k = sol.removeElement(nums_copy, t["input"]["val"])
        result_nums = nums_copy[:result_k]

        # Sorting both for comparison since order can vary
        pass_condition = (
            result_k == t["expected_k"] and
            sorted(result_nums) == sorted(t["expected_nums"])
        )

        print(
            f"Test {i}: nums={t['input']['nums']}, val={t['input']['val']} "
            f"=> result_k={result_k}, expected_k={t['expected_k']}, "
            f"result_nums={result_nums}, expected_nums={t['expected_nums']}, "
            f"{'✅ PASS' if pass_condition else '❌ FAIL'}"
        )
