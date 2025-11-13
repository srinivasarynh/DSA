# Problem: 1. Two sum
# LeetCode: https://leetcode.com/problems/two-sum/description/
# Author: srinivas
# Date: 2025-11-13
# Language: Python3


class Solution:
    def twoSum(self, nums: list[int], target: int) -> list[int]:
        # Your code here
        occurance = dict()
        for idx, num in enumerate(nums):
            diffrence = target - num
            if diffrence in occurance:
                return [occurance[diffrence], idx]
            occurance[num] = idx

        return []


if __name__ == "__main__":
    sol = Solution()
    tests = [
        {"input": ([2, 7, 11, 15], 9), "expected": [0, 1]},
        {"input": ([3, 2, 4], 6), "expected": [1, 2]},
        {"input": ([3, 3], 6), "expected": [0, 1]},
        {"input": ([1, 2, 3, 4, 5], 10), "expected": []},
        {"input": ([0, 4, 3, 0], 0), "expected": [0, 3]},
    ]

    for i, t in enumerate(tests, 1):
        result = sol.twoSum(*t["input"])
        print(
            f"Test {i}: result={result}, expected={t['expected']}, {'✅ PASS' if result==t['expected'] else '❌ FAIL'}"
        )
