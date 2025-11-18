# problem: 1646. Get maximum in generated array
# leetcode: https://leetcode.com/problems/get-maximum-in-generated-array/description/
# author: srinivas
# date: 2025-11-18
# language: python3


class Solution:
    def getMaximumGenerated(self, n: int) -> int:
        if n == 0:
            return 0
        if n == 1:
            return 1

        nums = [0] * (n + 1)
        nums[1] = 1
        for i in range(2, n+1):
            if i % 2 == 0:
                nums[i] = nums[i//2]
            else:
                nums[i] = nums[i//2]+nums[i//2+1]

        return max(nums)

# --------------------------
# Test cases
# --------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (input, expected_output)
        (0, 0),
        (1, 1),
        (2, 1),
        (3, 2),
        (4, 2),
        (5, 3),
        (6, 3),
        (7, 3),
        (10, 3),
        (15, 5),
        (50, 11),
        (100, 21),
    ]

    for i, (n, expected) in enumerate(tests, 1):
        result = sol.getMaximumGenerated(n)
        print(f"Test {i}: n={n}")
        print(f"  Expected: {expected}, Got: {result}")
        print("  PASS" if result == expected else "  FAIL")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
