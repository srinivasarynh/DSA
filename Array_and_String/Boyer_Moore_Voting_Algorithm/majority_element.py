# problem: 169. majority element
# leetcode: https://leetcode.com/problems/majority-element/
# author: srinivas
# date: 2025-11-19
# language: python3


class Solution:
    def majorityElement(self, nums):
        """
        :type nums: List[int]
        :rtype: int
        """
        count = 0
        candidate = None
        for n in nums:
            if count == 0:
                candidate = n

            count += (1 if n == candidate else -1)

        return candidate

# --------------------------
# Test Cases
# --------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (nums, expected_output)
        ([3, 2, 3], 3),
        ([2, 2, 1, 1, 1, 2, 2], 2),
        ([1], 1),
        ([1, 1, 1, 1], 1),
        ([2, 2, 2, 3, 3], 2),
        ([6, 5, 5], 5),
        ([-1, -1, -1, 2, 3], -1),
        ([0, 0, 0, 1], 0),
        ([10, 9, 10], 10),
        ([4, 4, 2, 4, 3, 4, 4], 4),
    ]

    for i, (nums, expected) in enumerate(tests, 1):
        result = sol.majorityElement(nums.copy())
        print(f"Test {i}: nums={nums}")
        print(f"  Expected: {expected}")
        print(f"  Got     : {result}")
        print("  PASS" if result == expected else "  FAIL")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
