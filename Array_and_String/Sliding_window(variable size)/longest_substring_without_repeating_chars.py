# problem: 3. Longest substring without repeating characters
# leetcode: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
# author: srinivas
# date: 2025-11-17
# language: python3


class Solution:
    def lengthOfLongestSubstring(self, s: str) -> int:
        # TODO: Replace this with your own implementation
        # Reference implementation included

        left = 0
        max_len = 0
        dist_char = set()

        for right in range(len(s)):
            while s[right] in dist_char:
                dist_char.remove(s[left])
                left += 1

            dist_char.add(s[right])
            max_len = max(max_len, right-left+1)

        return max_len

# ---------------------------------------------------------
# Test Harness
# ---------------------------------------------------------


def run_tests():
    sol = Solution()

    tests = [
        # (s, expected)

        # Basic examples
        ("abcabcbb", 3),             # "abc"
        ("bbbbb", 1),                # "b"
        ("pwwkew", 3),               # "wke"

        # Edge cases
        ("", 0),
        ("a", 1),
        ("aa", 1),
        ("ab", 2),

        # All characters unique
        ("abcdef", 6),

        # Repeating shifts
        ("abba", 2),                 # "ab" or "ba"
        ("tmmzuxt", 5),              # "mzuxt"

        # Alternating pattern
        ("abababab", 2),

        # Mixed cases
        ("dvdf", 3),                 # "vdf"
        ("anviaj", 5),               # "nviaj"

        # Unicode tests
        ("😀😃😄😁😆😅😂🤣☺️😊", 11),
        ("😀😃😃😀", 2),

        # Long tricky patterns
        ("abcdeafghijka", 11),       # "bcdeafghijk"
        ("aabcbcbb", 3),             # "abc"

        # Stress small patterns
        ("xyzxyzxyz", 3),
        ("longestsubstringtest", 8),  # "ubstring"

        # Contains spaces
        ("a b c a b", 3),
    ]

    for i, (s, expected) in enumerate(tests, 1):
        result = sol.lengthOfLongestSubstring(s)
        print(f"Test {i}: ", end="")
        if result == expected:
            print(f"PASS (result={result})")
        else:
            print(f"FAIL (result={result}, expected={expected})")


if __name__ == "__main__":
    run_tests()
