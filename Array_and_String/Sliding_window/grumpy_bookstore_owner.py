# problem: 1052. Grumpy bookstore owner
# leetcode: https://leetcode.com/problems/grumpy-bookstore-owner/description/
# author: srinivas
# date: 2025-11-17
# language: python3


from typing import List


class Solution:
    def maxSatisfied(self, customers: List[int], grumpy: List[int], minutes: int) -> int:
        # TODO: replace this stub with your implementation
        # Example reference implementation:

        left = 0
        window_sum = 0
        max_sum = 0
        satisfied = 0

        for right in range(len(customers)):
            if grumpy[right]:
                window_sum += customers[right]
            else:
                satisfied += customers[right]

            if right - left + 1 > minutes:
                if grumpy[left]:
                    window_sum -= customers[left]
                left += 1

            max_sum = max(window_sum, max_sum)

        return satisfied + max_sum

# -----------------------------------------
# Test Harness
# -----------------------------------------


def run_tests():
    sol = Solution()

    tests = [
        # Each test: (customers, grumpy, minutes, expected)
        ([1, 0, 1, 2, 1, 1, 7, 5], [0, 1, 0, 1, 0, 1, 0, 1], 3, 16),
        ([1], [0], 1, 1),
        ([1], [1], 1, 1),
        ([4, 10, 10], [1, 1, 0], 2, 24),
        ([2, 6, 6, 9], [0, 1, 1, 1], 1, 11),
        ([5, 8, 8, 5], [1, 1, 1, 1], 2, 16),
    ]

    for i, (customers, grumpy, minutes, expected) in enumerate(tests, 1):
        result = sol.maxSatisfied(customers, grumpy, minutes)
        print(f"Test {i}: ", end="")
        if result == expected:
            print(f"PASS (result={result})")
        else:
            print(f"FAIL (result={result}, expected={expected})")


if __name__ == "__main__":
    run_tests()
