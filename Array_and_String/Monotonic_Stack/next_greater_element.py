# Problem: 496. Next Greater Element I
# LeetCode: https://leetcode.com/problems/next-greater-element-i/description/
# Author: srinivas
# Date: 2025-11-19
# Language: Python3


class Solution:
    def nextGreaterElement(self, nums1, nums2):
        """
        :type nums1: List[int]
        :type nums2: List[int]
        :rtype: List[int]
        """

        stack = []
        next_greater = dict()

        for num in nums2:
            while stack and num > stack[-1]:
                next_greater[stack.pop()] = num
            stack.append(num)

        while stack:
            next_greater[stack.pop()] = -1

        return [next_greater[num] for num in nums1]

# --------------------------
# Test Cases
# --------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (nums1, nums2, expected_output)
        ([4, 1, 2], [1, 3, 4, 2], [-1, 3, -1]),
        ([2, 4], [1, 2, 3, 4], [3, -1]),
        ([1], [1], [-1]),
        ([3], [1, 2, 3], [-1]),
        ([2, 1], [1, 2], [-1, 2]),
        ([2, 1, 3], [2, 3, 1], [3, 3, -1]),
        ([4, 1, 2], [2, 1, 2, 4, 1, 3], [-1, 2, -1]),
        ([1, 3, 5, 2, 4], [6, 5, 4, 3, 2, 1, 7], [7, 7, 7, 7, 7]),
        ([], [1, 2, 3], []),
        ([1, 2], [2, 1], [-1, -1]),
    ]

    for i, (nums1, nums2, expected) in enumerate(tests, 1):
        result = sol.nextGreaterElement(nums1, nums2)
        print(f"Test {i}: nums1={nums1}, nums2={nums2}")
        print(f"  Expected: {expected}, Got: {result}")
        print("  PASS" if result == expected else "  FAIL")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
