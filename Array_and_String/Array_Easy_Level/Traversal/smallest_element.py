
# Problem: Find the Smallest Element in an Array
# LeetCode (or Custom):
# # Author: srinivas
# Date: 2025-11-12
# Language: Python3

class Solution:
    def findSmallest(self, nums):
        if len(nums) == 0:
            return None

        smallest_element = nums[0]
        for element in nums:
            if element < smallest_element:
                smallest_element = element

        return smallest_element


# --------- Local Test Harness ---------
if __name__ == "__main__":
    sol = Solution()

    tests = [
        {"input": [3, 5, 1, 8, 2], "expected": 1},
        {"input": [10, 10, 10], "expected": 10},
        {"input": [-5, -2, -9, -1], "expected": -9},
        {"input": [42], "expected": 42},
        # Optional: define how to handle empty array
        {"input": [], "expected": None},
    ]

    for i, t in enumerate(tests, 1):
        result = sol.findSmallest(t["input"])
        print(
            f"Test {i}: input={t['input']}, result={result}, expected={t['expected']}, "
            f"{'✅ PASS' if result == t['expected'] else '❌ FAIL'}"
        )
