# 1361 · 文字并排
# https://www.lintcode.com/problem/1361/description?utm_source=sc-libao-zyq
# Hard


from typing import (
    List,
)


class Solution:
    def _format(self, line, maxWidth):
        if len(line) == 1:
            return line[0] + " " * (maxWidth - len(line[0]))
        length = sum([len(w) for w in line])
        s, gaps = line[0], len(line) - 1
        for index, w in enumerate(line[1:]):
            if index < (maxWidth - length) % gaps:
                s = s + " " + " " * ((maxWidth - length) // gaps) + w
            else:
                s = s + " " * ((maxWidth - length) // gaps) + w
        return s

    def _formatLast(self, line, maxWidth):
        s = ' '.join(line)
        return s + " " * (maxWidth - len(s))

    # @param {string[]} words
    # @param {integer} maxWidth
    # @return {string[]}
    def full_justify(self, words, maxWidth):
        line, length = [], 0
        results = []
        for w in words:
            if length + len(w) + len(line) <= maxWidth:
                length += len(w)
                line.append(w)
            else:
                results.append(self._format(line, maxWidth))
                length = len(w)
                line = [w]
        if len(line):
            results.append(self._formatLast(line, maxWidth))
        return results