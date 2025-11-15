# problem: 974. subarray sum divisible by k
# leetcode: https://leetcode.com/problems/subarray-sums-divisible-by-k/description/
# author: srinivas
# date: 2025-11-15
# language: python3

from collections import defaultdict


class Solution:
    def subarraysDivByK(self, nums: list[int], k: int) -> int:
        # Your code here
        res = 0
        prefix_sum = 0
        prefix_cnt = defaultdict(int)
        prefix_cnt[0] = 1

        for num in nums:
            prefix_sum += num
            remain = prefix_sum % k

            res += prefix_cnt[remain]
            prefix_cnt[remain] += 1

        return res


if __name__ == "__main__":
    sol = Solution()
    tests = [
        {"input": ([4, 5, 0, -2, -3, 1], 5), "expected": 7},
        {"input": ([5], 5), "expected": 1},
        {"input": ([1, 2, 3], 3), "expected": 3},
        {"input": ([2, -2, 2, -4], 6), "expected": 2},
        {"input": ([7, 4, -10], 5), "expected": 1},
        {"input": ([0, 0, 0], 1), "expected": 6},
        {"input": ([0], 5), "expected": 1},
        {"input": ([], 3), "expected": 0},
        {"input": ([23, 2, 4, 6, 7], 6), "expected": 4},
        {"input": ([1, -1, 1, -1], 2), "expected": 4},
    ]

    for i, t in enumerate(tests, 1):
        result = sol.subarraysDivByK(*t["input"])
        print(
            f"Test {i}: result={result}, expected={t['expected']}, {'✅ PASS' if result == t['expected'] else '❌ FAIL'}"
        )
