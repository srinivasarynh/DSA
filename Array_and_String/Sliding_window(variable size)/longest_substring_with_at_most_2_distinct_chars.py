# problem: -. Longest substring with at most 2 distinct characters
# leetcode: -
# author: srinivas
# date: 2025-11-17
# language: python3


class Solution:
    def lengthOfLongestSubstringTwoDistinct(self, s: str) -> int:
        # TODO: replace this stub with your own implementation
        # Reference implementation included
        left = 0
        max_len = 0
        char_dict = dict()

        for right in range(len(s)):
            char_dict[s[right]] = right

            if len(char_dict) > 2:
                leftmost_index = min(char_dict.values())
                del char_dict[s[leftmost_index]]
                left = leftmost_index + 1

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
        ("eceba", 3),              # "ece"
        ("ccaabbb", 5),            # "aabbb"

        # Edge cases
        ("", 0),
        ("a", 1),
        ("aa", 2),
        ("ab", 2),

        # All same character
        ("aaaaa", 5),

        # All distinct except two
        ("abc", 2),
        ("abca", 3),               # "bca"

        # Multiple changes
        ("abababab", 8),
        ("abcbbbbcccbdddadacb", 10),  # classic test, "bcbbbbcccb"

        # Mixed patterns
        ("aabbcc", 4),             # "aabb" or "bbcc"
        ("aabacbebebe", 6),        # "bebebe"
        ("abaccc", 4),             # "accc"

        # Repeating patterns
        ("abcabcabc", 2),
        ("abaac", 4),              # "abaa"

        # Long runs with short interruptions
        ("aaaaabbbbbc", 10),       # "aaaaabbbbb"
        ("abcbbbbcccbdddadacb", 10),

        # Tight boundary flips
        ("abbbbaaaccc", 6),        # "bbbbaa" or "aaaccc"
    ]

    for i, (s, expected) in enumerate(tests, 1):
        result = sol.lengthOfLongestSubstringTwoDistinct(s)
        print(f"Test {i}: ", end="")
        if result == expected:
            print(f"PASS (result={result})")
        else:
            print(f"FAIL (result={result}, expected={expected})")


if __name__ == "__main__":
    run_tests()
