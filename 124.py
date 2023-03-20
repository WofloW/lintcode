from typing import (
    List,
)


class Solution:
    """
    @param num: A list of integers
    @return: An integer
    """

    def longest_consecutive(self, num: List[int]) -> int:
        # write your code here

        s = set(num)
        result = 0
        for n in s:
            # Only count the streak number when the number is a head of consecutive sequence
            # For example, 1 2 3 4 Don't enter the loop if we see 2 3 4
            # So that we can achieve O(n) time complexity
            if n - 1 not in s:
                current = n
                streak = 1
                # Count the streak to the right
                while current + 1 in s:
                    current += 1
                    streak += 1
                result = max(result, streak)
        return result


