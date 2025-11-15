# problem: 560. Subarray sum equals K
# leetcode: https://leetcode.com/problems/subarray-sum-equals-k/description/
# author: srinivas
# date: 2025-11-15
# language: python3


class Solution:
    def subarraySum(self, nums: list[int], k: int) -> int:
        # Your code here
        res = 0
        curSum = 0
        prefixSum = dict({0: 1})

        for num in nums:
            curSum += num
            diff = curSum - k

            res += prefixSum.get(diff, 0)
            prefixSum[curSum] = 1 + prefixSum.get(curSum, 0)

        return res


if __name__ == "__main__":
    sol = Solution()
    tests = [
        {"input": ([1, 1, 1], 2), "expected": 2},
        {"input": ([1, 2, 3], 3), "expected": 2},
        {"input": ([1, -1, 0], 0), "expected": 3},
        {"input": ([3, 4, 7, 2, -3, 1, 4, 2], 7), "expected": 4},
        {"input": ([0, 0, 0, 0, 0], 0), "expected": 15},
        {"input": ([1, 2, 1, 2, 1], 3), "expected": 4},
        {"input": ([10, 2, -2, -20, 10], -10), "expected": 3},
        {"input": ([1], 0), "expected": 0},
        {"input": ([1], 1), "expected": 1},
        {"input": ([], 0), "expected": 0},
    ]

    for i, t in enumerate(tests, 1):
        result = sol.subarraySum(*t["input"])
        print(
            f"Test {i}: result={result}, expected={t['expected']}, {'✅ PASS' if result==t['expected'] else '❌ FAIL'}"
        )
