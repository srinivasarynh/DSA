# Problem: Find the Sum of All Elements in an Array
# LeetCode (or Custom): https://www.geeksforgeeks.org/dsa/program-find-sum-elements-given-array/
# Author: srinivas
# Date: 2025-11-12
# Language: Python3

class Solution:
    def sumOfElements(self, nums):
        """
        Given an array of integers, return the sum of all its elements.
        Example:
        Input: [1, 2, 3, 4, 5]
        Output: 15
        """
        # 🧠 TODO: Write your code here
        if len(nums) == 0:
            return 0

        sum = 0
        for element in nums:
            sum = sum + element

        return sum


# --------- Local Test Harness ---------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        {"input": [1, 2, 3, 4, 5], "expected": 15},
        {"input": [10, 10, 10], "expected": 30},
        {"input": [-5, 5, -10, 10], "expected": 0},
        {"input": [0], "expected": 0},
        {"input": [], "expected": 0},  # Optional: define empty array behavior
    ]

    for i, t in enumerate(tests, 1):
        result = sol.sumOfElements(t["input"])
        print(
            f"Test {i}: input={t['input']}, result={result}, expected={t['expected']}, "
            f"{'✅ PASS' if result == t['expected'] else '❌ FAIL'}"
        )
