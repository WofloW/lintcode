# 643 · 最长绝对文件路径
# https://www.lintcode.com/problem/643/description?fromId=18&_from=collection

# 模拟版 无优化
class Solution:
    """
    @param input: an abstract file system
    @return: return the length of the longest absolute path to file
    """

    def length_longest_path(self, input: str) -> int:
        # write your code here
        path = []
        items = input.split('\\n')
        max_len = 0
        for item in items:
            level = item.count('\\t')
            while level < len(path):
                path.pop()
            path.append(item.replace('\\t', ''))

            if item.find('.') != -1:
                current_path = '/'.join(path)
                max_len = max(max_len, len(current_path))

        return max_len

# 有优化版，记录了每一层的已有长度
class Solution1:
    """
    @param input: an abstract file system
    @return: return the length of the longest absolute path to file
    """

    def length_longest_path(self, input: str) -> int:
        # write your code here
        len_of_levels = collections.defaultdict(int)
        items = input.split('\\n')
        max_len = 0
        for item in items:
            parts = item.split('\\t')
            level = len(parts)
            current_len = len(parts[-1])

            if '.' in item:
                current_total_len = len_of_levels[level - 1] + current_len
                max_len = max(max_len, current_total_len)
            else:
                # add 1 because we need add / for dir
                current_len += 1
                len_of_levels[level] = len_of_levels[level - 1] + current_len

        return max_len