# problem: 1480. Running Sum of 1d Array
# leetcode: https://leetcode.com/problems/running-sum-of-1d-array/description/
# author: srinivas
# date: 2025-11-13
# language: python3

class Solution:
    def runningSum(self, nums: list[int]) -> list[int]:
        # Your code here
        if not nums:
            return []

        result = [0] * len(nums)
        result[0] = nums[0]

        for idx in range(1, len(nums)):
            result[idx] = result[idx-1] + nums[idx]

        return result


if __name__ == "__main__":
    sol = Solution()
    tests = [
        {"input": ([1, 2, 3, 4],), "expected": [1, 3, 6, 10]},
        {"input": ([1, 1, 1, 1, 1],), "expected": [1, 2, 3, 4, 5]},
        {"input": ([3, 1, 2, 10, 1],), "expected": [3, 4, 6, 16, 17]},
        {"input": ([0, 0, 0, 0],), "expected": [0, 0, 0, 0]},
        {"input": ([],), "expected": []},
    ]

    for i, t in enumerate(tests, 1):
        result = sol.runningSum(*t["input"])
        print(
            f"Test {i}: result={result}, expected={t['expected']}, {'✅ PASS' if result==t['expected'] else '❌ FAIL'}"
        )
