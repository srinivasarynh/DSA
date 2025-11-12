# Problem: 1. Two Sum
# LeetCode: https://leetcode.com/problems/two-sum/
# Author: srinivas
# Date: 2025-11-12
# Language: Python3

"""
Given an array of integers nums and an integer target, return indices of the two numbers
such that they add up to target.

You may assume that each input would have exactly one solution, and you may not use the same
element twice.

You can return the answer in any order.

Example 1:
Input: nums = [2,7,11,15], target = 9
Output: [0,1]
Explanation: Because nums[0] + nums[1] == 9, we return [0, 1].

Example 2:
Input: nums = [3,2,4], target = 6
Output: [1,2]

Example 3:
Input: nums = [3,3], target = 6
Output: [0,1]

Constraints:
- 2 <= nums.length <= 10^4
- -10^9 <= nums[i] <= 10^9
- -10^9 <= target <= 10^9
- Only one valid answer exists.

Follow-up: Can you come up with an algorithm that is less than O(n^2) time complexity?
"""


class Solution:
    def twoSum(self, nums, target):
        """
        Given a list of integers nums and a target value,
        return the indices of the two numbers that add up to the target.
        """
        # 🧠 TODO: Write your code here

        # Brute force approach:
        """
        if len(nums) == 0:
            return []

        for i in range(len(nums)):
            for j in range(i+1, len(nums)):
                sum = nums[i] + nums[j]
                if sum == target:
                    return [i, j]

        return []
        """
        # optimised using dictionary
        if len(nums) == 0:
            return []

        mymap = {}
        for idx, element in enumerate(nums):
            diff = target - element
            if diff in mymap:
                return [mymap[diff], idx]
            mymap[element] = idx

        return []


# --------- Local Test Harness ---------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        {"input": {"nums": [2, 7, 11, 15], "target": 9}, "expected": [0, 1]},
        {"input": {"nums": [3, 2, 4], "target": 6}, "expected": [1, 2]},
        {"input": {"nums": [3, 3], "target": 6}, "expected": [0, 1]},
    ]

    for i, t in enumerate(tests, 1):
        result = sol.twoSum(**t["input"])
        print(
            f"Test {i}: nums={t['input']['nums']}, target={t['input']['target']} "
            f"=> result={result}, expected={t['expected']}, "
            f"{'✅ PASS' if result == t['expected'] else '❌ FAIL'}"
        )
