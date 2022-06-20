# 1378 · 最小字符串数组覆盖
# https://www.lintcode.com/problem/1378/description?fromId=15&_from=collection
# Medium

# two pointer and hashmap
from typing import (
    List,
)


class Solution:
    """
    @param tag_list: The tag list.
    @param all_tags: All the tags.
    @return: Return the answer
    """

    def get_minimum_string_array(self, tag_list: List[str], all_tags: List[str]) -> int:
        # Write your code here
        counter = collections.Counter(tag_list)
        result = float('inf')
        left = right = 0
        covered_cnt = 0
        n = len(tag_list)
        for right, tag in enumerate(all_tags):
            if covered_cnt < n:
                if tag in counter:
                    counter[tag] -= 1
                    if counter[tag] >= 0:
                        covered_cnt += 1

            while covered_cnt == n:
                result = min(result, right - left + 1)
                if all_tags[left] in counter:
                    counter[all_tags[left]] += 1
                    if counter[all_tags[left]] > 0:
                        covered_cnt -= 1
                left += 1
        return result if result != float('inf') else -1