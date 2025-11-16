# problem: 42. Trapping rain water
# leetcode: https://leetcode.com/problems/trapping-rain-water/description/
# author: srinivas
# date: 2025-11-16
# language: python3


from typing import List


class Solution:
    def trap(self, height: List[int]) -> int:
        """
        Two-pointer approach.
        Computes the total units of water that can be trapped.
        """
        left, right = 0, len(height)-1
        left_max, right_max = 0, 0
        water = 0

        while (left < right):
            if height[left] < height[right]:
                if height[left] >= left_max:
                    left_max = height[left]
                else:
                    water += left_max - height[left]
                left += 1
            else:
                if height[right] >= right_max:
                    right_max = height[right]
                else:
                    water += right_max - height[right]
                right -= 1

        return water

# -------------------------
# Test Cases
# -------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (height list, expected result)
        ([0, 1, 0, 2, 1, 0, 1, 3, 2, 1, 2, 1], 6),
        ([4, 2, 0, 3, 2, 5], 9),
        ([1, 0, 1], 1),
        ([2, 0, 2], 2),
        ([3, 0, 0, 2, 0, 4], 10),
        ([], 0),
        ([1], 0),
        ([1, 2, 3, 4, 5], 0),             # Increasing → no water
        ([5, 4, 3, 2, 1], 0),             # Decreasing → no water
        ([2, 1, 0, 1, 3], 5),
        ([0, 0, 0], 0),
        ([1, 7, 8], 0),
        ([5, 2, 1, 2, 1, 5], 14),
        ([4, 9, 4, 5, 3, 2], 1),
        ([2, 2, 2, 2], 0),               # Flat → no water
        ([6, 0, 5, 0, 4], 9),
    ]

    for i, (heights, expected) in enumerate(tests, 1):
        result = sol.trap(heights)
        print(f"Test {i}:")
        print(f" Input:  {heights}")
        print(f" Output: {result}")
        print(f" Expected: {expected}")
        print(" Pass:", result == expected)
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
