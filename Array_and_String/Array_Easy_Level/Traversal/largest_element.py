# Problem: Find the Largest Element in an Array
# LeetCode (or Custom): https://www.geeksforgeeks.org/problems/largest-element-in-array4009/1
# Author: srinivas
# Date: 2025-11-12
# Language: Python3

class Solution:
    def findLargest(self, nums):
        if len(nums) == 0:
            return None

        largest_element = nums[0]
        for element in nums:
            if element > largest_element:
                largest_element = element

        return largest_element


# --------- Local Test Harness ---------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        {"input": [3, 5, 1, 8, 2], "expected": 8},
        {"input": [10, 10, 10], "expected": 10},
        {"input": [-5, -2, -9, -1], "expected": -1},
        {"input": [42], "expected": 42},
        # Optional: define how to handle empty array
        {"input": [], "expected": None},
    ]

    for i, t in enumerate(tests, 1):
        result = sol.findLargest(t["input"])
        print(
            f"Test {i}: input={t['input']}, result={result}, expected={t['expected']}, {'✅ PASS' if result==t['expected'] else '❌ FAIL'}")
