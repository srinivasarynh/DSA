# problem: 88. Merge Sorted Array
# leetcode: https://leetcode.com/problems/merge-sorted-array/description/
# author: srinivas
# date: 2025-11-16
# language: python3


from typing import List


class Solution:
    def merge(self, nums1: List[int], m: int, nums2: List[int], n: int) -> None:
        """
        Merges nums2 into nums1 in-place.
        nums1 has length m+n, with the last n elements empty (0 placeholders).
        """
        p1 = m - 1
        p2 = n - 1
        p = m+n-1

        while p2 >= 0:
            if p1 >= 0 and nums1[p1] > nums2[p2]:
                nums1[p] = nums1[p1]
                p1 -= 1
            else:
                nums1[p] = nums2[p2]
                p2 -= 1
            p -= 1

# -------------------------
# Test Cases
# -------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (nums1, m, nums2, n, expected)
        ([1, 2, 3, 0, 0, 0], 3, [2, 5, 6], 3, [1, 2, 2, 3, 5, 6]),
        ([1], 1, [], 0, [1]),
        ([0], 0, [1], 1, [1]),
        ([2, 0], 1, [1], 1, [1, 2]),
        ([4, 5, 6, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 4, 5, 6]),
        ([1, 2, 4, 5, 6, 0], 5, [3], 1, [1, 2, 3, 4, 5, 6]),
        ([0, 0, 0], 0, [2, 5, 7], 3, [2, 5, 7]),
        ([1, 1, 1, 0, 0, 0], 3, [1, 1, 1], 3, [1, 1, 1, 1, 1, 1]),
        ([1, 3, 5, 0, 0, 0], 3, [2, 4, 6], 3, [1, 2, 3, 4, 5, 6]),
        ([1, 2, 3, 0, 0], 3, [4, 5], 2, [1, 2, 3, 4, 5]),
        ([3, 4, 5, 0, 0, 0], 3, [-3, -1, 2], 3, [-3, -1, 2, 3, 4, 5]),
        ([5, 6, 7, 0, 0, 0], 3, [1, 2, 3], 3, [1, 2, 3, 5, 6, 7]),
    ]

    for i, (nums1, m, nums2, n, expected) in enumerate(tests, 1):
        arr = nums1[:]  # copy so we don't mutate original test definition
        sol.merge(arr, m, nums2, n)
        print(f"Test {i}:")
        print(f" nums1:    {nums1}")
        print(f" nums2:    {nums2}")
        print(f" Output:   {arr}")
        print(f" Expected: {expected}")
        print(" Pass:", arr == expected)
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
