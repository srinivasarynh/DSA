# Problem: 503. Next greater element II
# LeetCode: https://leetcode.com/problems/next-greater-element-ii/description/
# Author: srinivas
# Date: 2025-11-19
# Language: Python3


class Solution:
    def nextGreaterElements(self, nums):
        """
        :type nums: List[int]
        :rtype: List[int]
        """
        n = len(nums)
        result = [-1] * len(nums)
        stack = []

        for i in range(2*n):
            while stack and nums[i % n] > nums[stack[-1]]:
                idx = stack.pop()
                result[idx] = nums[i % n]

            if i < n:
                stack.append(i)

        return result

# --------------------------
# Test Cases
# --------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (nums, expected_output)
        ([1, 2, 1], [2, -1, 2]),
        ([1, 2, 3, 4, 3], [2, 3, 4, -1, 4]),
        ([5, 4, 3, 2, 1], [-1, 5, 5, 5, 5]),
        ([2, 2, 2], [-1, -1, -1]),
        ([3], [-1]),
        ([1, 2], [2, -1]),
        ([2, 1], [-1, 2]),
        ([1, 5, 3, 6, 8], [5, 6, 6, 8, -1]),
        ([10, 9, 8, 7, 11], [11, 11, 11, 11, -1]),
        ([6, 5, 4, 3, 2, 7], [7, 7, 7, 7, 7, -1]),
    ]

    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.nextGreaterElements(nums.copy())
        print(f"Test {i}: nums={nums}")
        print(f"  Expected: {expected}")
        print(f"  Got     : {result}")
        print("  PASS" if result == expected else "  FAIL")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
