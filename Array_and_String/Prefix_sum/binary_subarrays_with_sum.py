# problem: 930. Binary subarrays with sum
# leetcode: https://leetcode.com/problems/binary-subarrays-with-sum/
# author: srinivas
# date: 2025-11-15
# language: python3

class Solution:
    def numSubarraysWithSum(self, nums: list[int], goal: int) -> int:
        # Your code here
        if not nums:
            return 0

        res = 0
        prefix_sum = 0
        prefix_dict = dict({0: 1})

        for num in nums:
            prefix_sum += num
            diff = prefix_sum - goal

            res += prefix_dict.get(diff, 0)
            prefix_dict[prefix_sum] = 1 + prefix_dict.get(prefix_sum, 0)

        return res


if __name__ == "__main__":
    sol = Solution()
    tests = [
        {"input": ([1, 0, 1, 0, 1], 2), "expected": 4},
        {"input": ([0, 0, 0, 0, 0], 0), "expected": 15},
        {"input": ([0, 0, 1, 0], 1), "expected": 4},
        {"input": ([1, 1, 1], 2), "expected": 2},
        {"input": ([1], 1), "expected": 1},
        {"input": ([1], 0), "expected": 0},
        {"input": ([0], 0), "expected": 1},
        {"input": ([0], 1), "expected": 0},
        {"input": ([], 0), "expected": 0},
        {"input": ([1, 0, 1, 1, 0, 1], 3), "expected": 3},
        {"input": ([0, 1, 0, 1, 0, 1, 0], 2), "expected": 6},
    ]

    for i, t in enumerate(tests, 1):
        result = sol.numSubarraysWithSum(*t["input"])
        print(
            f"Test {i}: result={result}, expected={t['expected']}, {'✅ PASS' if result == t['expected'] else '❌ FAIL'}"
        )
