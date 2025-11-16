# problem: 11. Container with most water
# leetcode: https://leetcode.com/problems/container-with-most-water/description/
# author: srinivas
# date: 2025-11-16
# language: python3


from typing import List


class Solution:
    def maxArea(self, height: List[int]) -> int:
        """
        Two-pointer approach.
        Returns the maximum water area between two vertical lines.
        """
        left = 0
        right = len(height)-1
        max_area = 0

        while (left < right):
            h = min(height[left], height[right])
            w = right - left
            current_area = h * w
            max_area = max(max_area, current_area)

            if height[left] < height[right]:
                left += 1
            else:
                right -= 1

        return max_area
# -------------------------
# Test Cases
# -------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (height list, expected result)
        ([1, 8, 6, 2, 5, 4, 8, 3, 7], 49),
        ([1, 1], 1),
        ([4, 3, 2, 1, 4], 16),
        ([1, 2, 1], 2),
        ([2, 3, 4, 5, 18, 17, 6], 17),
        ([1, 3, 2, 5, 25, 24, 5], 24),
        ([1], 0),                # Single line → zero area
        ([], 0),                 # Empty input
        ([2, 2, 2, 2, 2], 8),        # All same height
        ([1, 2, 4, 3], 4),
        ([10, 9, 8, 7, 6, 5, 4, 3, 2, 1], 25),
    ]

    for i, (heights, expected) in enumerate(tests, 1):
        result = sol.maxArea(heights)
        print(f"Test {i}:")
        print(f" Input: {heights}")
        print(f" Output: {result}")
        print(f" Expected: {expected}")
        print(" Pass:", result == expected)
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
