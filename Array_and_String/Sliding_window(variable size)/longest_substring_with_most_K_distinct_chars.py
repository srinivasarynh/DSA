# problem: -. Longest substring with at most K distinct characters
# leetcode:
# author: srinivas
# date: 2025-11-17
# language: python3


class Solution:
    def lengthOfLongestSubstringKDistinct(self, s: str, k: int) -> int:
        # TODO: replace this stub with your own implementation
        # Reference implementation included for convenience

        if k == 0:
            return 0

        left = 0
        count = dict()
        max_len = 0

        for right, ch in enumerate(s):
            count[ch] = count.get(ch, 0) + 1

            while len(count) > k:
                left_ch = s[left]
                count[left_ch] -= 1
                if count[left_ch] == 0:
                    del count[left_ch]
                left += 1

            max_len = max(max_len, right-left+1)

        return max_len

# ---------------------------------------------------------
# Test Harness
# ---------------------------------------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (s, k, expected)

        # Basic examples
        ("eceba", 2, 3),      # "ece"
        ("aa", 1, 2),

        # Edge cases
        ("", 2, 0),
        ("a", 0, 0),
        ("a", 1, 1),
        ("abc", 0, 0),

        # Single distinct letter repeated
        ("aaaaa", 1, 5),
        ("bbbbbb", 2, 6),

        # All distinct, k small
        ("abcdef", 1, 1),
        ("abcdef", 2, 2),
        ("abcdef", 3, 3),

        # Mixed patterns
        ("abaccc", 2, 4),     # "accc"
        ("abcadcacacaca", 3, 11),

        # k larger than number of distinct characters
        ("abc", 10, 3),

        # Long mixed patterns
        ("aabbccddeeffgg", 2, 4),
        ("aabbccddeeffgg", 3, 6),
        ("aabacbebebe", 3, 7),  # "cbebebe"
    ]

    for i, (s, k, expected) in enumerate(tests, 1):
        result = sol.lengthOfLongestSubstringKDistinct(s, k)
        print(f"Test {i}: ", end="")
        if result == expected:
            print(f"PASS (result={result})")
        else:
            print(f"FAIL (result={result}, expected={expected})")


if __name__ == "__main__":
    run_tests()
