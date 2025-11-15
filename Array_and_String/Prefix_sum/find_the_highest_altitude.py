# problem: 1732. Find the highest altitude
# leetcode: https://leetcode.com/problems/find-the-highest-altitude/description/
# author: srinivas
# date: 2025-11-15
# language: python3


class Solution:
    def largestAltitude(self, gain: list[int]) -> int:
        # Your code here
        if not gain:
            return 0

        prefix_sum = [0] * len(gain)
        prefix_sum[0] = gain[0]

        for idx in range(1, len(gain)):
            prefix_sum[idx] = prefix_sum[idx-1] + gain[idx]

        if max(prefix_sum) > 0:
            return max(prefix_sum)
        else:
            return 0


if __name__ == "__main__":
    sol = Solution()
    tests = [
        {"input": ([-5, 1, 5, 0, -7],), "expected": 1},
        {"input": ((-4, -3, -2, -1, 4, 3, 2),), "expected": 0},
        {"input": ([1, 2, 3],), "expected": 6},
        {"input": ([],), "expected": 0},
        {"input": ([-1],), "expected": 0},
        {"input": ([0],), "expected": 0},
        {"input": ([-2, -1, -3],), "expected": 0},
    ]

    for i, t in enumerate(tests, 1):
        result = sol.largestAltitude(*t["input"])
        print(
            f"Test {i}: result={result}, expected={t['expected']}, {'✅ PASS' if result == t['expected'] else '❌ FAIL'}"
        )
