# problem: 152. Maximum Product subarray152. Maximum Product subarray152. Maximum Product subarray152. Maximum Product subarray152. Maximum Product subarray152. Maximum Product subarray152. Maximum Product subarray152. Maximum Product subarray152. Maximum Product subarray152. Maximum Product subarray152. Maximum Product subarray152. Maximum Product subarray152. Maximum Product subarray152. Maximum Product subarray152. Maximum Product subarray
# leetcode: https://leetcode.com/problems/maximum-product-subarray/description/
# author: srinivas
# date: 2025-11-18
# language: python3


class Solution:
    def maxProduct(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        if not nums:
            return 0

        cur_max = nums[0]
        cur_min = nums[0]
        result = nums[0]

        for num in nums[1:]:
            if num < 0:
                cur_max, cur_min = cur_min, cur_max

            cur_max = max(num, cur_max * num)
            cur_min = min(num, cur_min * num)
            result = max(result, cur_max)

        return result


# --------------------------
# Test Cases
# --------------------------

def run_tests():
    sol = Solution()

    tests = [
        # (input, expected_output)
        ([2, 3, -2, 4], 6),
        ([-2, 0, -1], 0),
        ([0], 0),
        ([-2], -2),
        ([2, -5, -2, -4, 3], 24),
        ([1, 2, 3, 4], 24),
        ([-1, -2, -3, -4], 24),
        ([0, 2], 2),
        ([3, -1, 4], 4),
        ([2, -1, 1, 1], 2),
        ([2, -2, -3, 0, -2, -40], 80),
        ([-2, -3, 7], 42),
        ([-2, 3, -4], 24),
        ([1, -2, 3, -4, 5, -6], 720),
    ]

    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.maxProduct(nums)
        print(f"Test {i}: nums={nums}")
        print(f"  Expected: {expected}, Got: {result}")
        print("  PASS" if result == expected else "  FAIL")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
