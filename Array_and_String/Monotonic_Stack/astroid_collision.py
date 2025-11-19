# Problem: 735. Asteroid collision
# LeetCode: https://leetcode.com/problems/asteroid-collision/description/
# Author: srinivas
# Date: 2025-11-19
# Language: Python3


class Solution:
    def asteroidCollision(self, asteroids):
        """
        :type asteroids: List[int]
        :rtype: List[int]
        """
        stack = []

        for a in asteroids:
            while stack and a < 0 and stack[-1] > 0:
                if stack[-1] < -a:
                    stack.pop()
                    continue
                elif stack[-1] == -a:
                    stack.pop()
                break
            else:
                stack.append(a)

        return stack
# --------------------------
# Test Cases
# --------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (asteroids, expected_output)
        ([5, 10, -5], [5, 10]),
        ([8, -8], []),
        ([10, 2, -5], [10]),
        ([-2, -1, 1, 2], [-2, -1, 1, 2]),
        ([1, -1, 2, -2], []),
        ([1, 2, 3, -3], [1, 2]),
        ([3, 5, -2, -1], [3, 5]),
        ([-5, -3, -1], [-5, -3, -1]),
        ([1], [1]),
        ([-1], [-1]),
        ([5, -10, 10, -5], [5, 10]),
        ([4, 3, 2, 1, -10], [-10]),
        ([10, -2, -2, -2], [10]),
    ]

    for i, (asteroids, expected) in enumerate(tests, 1):
        result = sol.asteroidCollision(asteroids.copy())
        print(f"Test {i}: asteroids={asteroids}")
        print(f"  Expected: {expected}")
        print(f"  Got     : {result}")
        print("  PASS" if result == expected else "  FAIL")
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
