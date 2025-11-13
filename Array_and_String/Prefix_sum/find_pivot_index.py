# problem: 724. Find Pivot index
# leetcode: https://leetcode.com/problems/find-pivot-index/description/
# author: srinivas
# date: 2025-11-13
# language: python3


class Solution:
    def pivotIndex(self, nums: list[int]) -> int:
        # Your code here
        leftsum, rightsum = 0, sum(nums)
        for idx, num in enumerate(nums):
            rightsum -= num
            if leftsum == rightsum:
                return idx
            leftsum += num
        return -1


if __name__ == "__main__":
    sol = Solution()
    tests = [
        {"input": ([1, 7, 3, 6, 5, 6],), "expected": 3},
        {"input": ([1, 2, 3],), "expected": -1},
        {"input": ([2, 1, -1],), "expected": 0},
        {"input": ([0, 0, 0, 0],), "expected": 0},
        {"input": ([1, -1, 0],), "expected": 2},
        {"input": ([20],), "expected": 0},
        {"input": ([],), "expected": -1},
        {"input": ([-1, -1, -1, 0, 1, 1],), "expected": 0},
    ]

    for i, t in enumerate(tests, 1):
        result = sol.pivotIndex(*t["input"])
        print(
            f"Test {i}: result={result}, expected={t['expected']}, {'✅ PASS' if result==t['expected'] else '❌ FAIL'}"
        )
