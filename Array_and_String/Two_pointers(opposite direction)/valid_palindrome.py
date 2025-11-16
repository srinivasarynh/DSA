# problem: 125. Valid Palindrome
# leetcode: https://leetcode.com/problems/valid-palindrome/description/
# author: srinivas
# date: 2025-11-16
# language: python3


class Solution:
    def isPalindrome(self, s: str) -> bool:
        """
        Returns True if s is a palindrome, considering only alphanumeric characters
        and ignoring cases.
        """
        left = 0
        right = len(s)-1

        while (left < right):
            while left < right and not s[left].isalnum():
                left += 1
            while left < right and not s[right].isalnum():
                right -= 1
            if s[left].lower() != s[right].lower():
                return False

            left += 1
            right -= 1

        return True

# -------------------------
# Test Cases
# -------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (input_string, expected_result)
        ("A man, a plan, a canal: Panama", True),
        ("race a car", False),
        (" ", True),
        ("0P", False),
        ("ab_a", True),
        ("Madam, in Eden, I'm Adam", True),
        ("No lemon, no melon", True),
        ("12321", True),
        ("1231", False),
    ]

    for i, (s, expected) in enumerate(tests, 1):
        result = sol.isPalindrome(s)
        print(f"Test {i}:")
        print(f" Input: {s!r}")
        print(f" Output: {result}")
        print(f" Expected: {expected}")
        print(" Pass:", result == expected)
        print("-" * 40)


if __name__ == "__main__":
    run_tests()
