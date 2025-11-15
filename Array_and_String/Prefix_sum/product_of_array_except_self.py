# problem: 238. Product of Array except slef
# leetcode: https://leetcode.com/problems/product-of-array-except-self/description/
# author: srinivas
# date: 2025-11-15
# language: python3


class Solution:
    def productExceptSelf(self, nums: list[int]) -> list[int]:
        # Your code here
        """
        res = [1] * len(nums)
        prefix = 1
        for i in range(len(nums)):
            res[i] = prefix
            prefix *= nums[i]

        postfix = 1
        for i in range(len(nums)-1, -1, -1):
            res[i] *= postfix
            postfix *= nums[i]

        return res
        """
        if not nums:
            return []

        left = [1] * len(nums)
        right = [1] * len(nums)

        left[0] = 1
        right[len(nums)-1] = 1

        for idx in range(1, len(nums)):
            left[idx] = left[idx-1] * nums[idx-1]

        for idx in range(len(nums)-2, -1, -1):
            right[idx] = right[idx+1] * nums[idx+1]

        ans = [1] * len(nums)
        for idx in range(len(nums)):
            ans[idx] = left[idx] * right[idx]

        return ans


if __name__ == "__main__":
    sol = Solution()
    tests = [
        {"input": ([1, 2, 3, 4],), "expected": [24, 12, 8, 6]},
        {"input": ([0, 1, 2, 3],), "expected": [6, 0, 0, 0]},
        {"input": ([0, 0, 3, 4],), "expected": [0, 0, 0, 0]},
        {"input": ([-1, 1, 0, -3, 3],), "expected": [0, 0, 9, 0, 0]},
        {"input": ([5],), "expected": [1]},
        {"input": ([2, 3],), "expected": [3, 2]},
        {"input": ([1, 0],), "expected": [0, 1]},
        {"input": ([],), "expected": []},
        {"input": ([10, 3, 5, 6, 2],), "expected": [180, 600, 360, 300, 900]},
    ]

    for i, t in enumerate(tests, 1):
        result = sol.productExceptSelf(*t["input"])
        print(
            f"Test {i}: result={result}, expected={t['expected']}, {'✅ PASS' if result == t['expected'] else '❌ FAIL'}"
        )
