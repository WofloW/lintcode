# 1017 · 相似的RGB颜色
# https://www.lintcode.com/problem/1017/?fromId=18&_from=collection

# 16进制的11 22 33都是17的倍数，余数大于8的应该更靠近下一个叠数
# 用'{:02x}'.format(q * 17) 或者 format(q * 17, '02x')能把这个数字转成十六进制字符串
# https://docs.python.org/2/library/string.html#formatspec
# 格式说明
# 02是说字符串长度为0，x是hex
class Solution:
    """
    @param color: the given color
    @return: a 7 character color that is most similar to the given color
    """
    def similar_r_g_b(self, color: str) -> str:
        # Write your code here
        def get_options(color):
            q, r = divmod(int(color, 16), 17)
            if r > 8:
                q += 1
            return format(q * 17, '02x')
        result_r = get_options(color[1:3])
        result_g = get_options(color[3:5])
        result_b = get_options(color[5:])
        return '#' + result_r + result_g + result_b