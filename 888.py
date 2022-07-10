# 888 · 有效单词方阵
# https://www.lintcode.com/problem/888/solution?fromId=18&_from=collection

class Solution:
    """
	@param words: a list of string
	@return: return a boolean
	"""

    def validWordSquare(self, words):
        # write your code here
        n, m = len(words), len(words[0])
        for i in range(m):
            for j in range(len(words[i])):
                if j >= m or i >= len(words[j]) or words[i][j] != words[j][i]:
                    return False
        return True
