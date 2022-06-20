# 1186 · TinyURL 的加密与解密
# https://www.lintcode.com/problem/1186/description?fromId=15&_from=collection


DIGIT = '0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ'
class Solution:
    def __init__(self):
        self.long_to_short = {}
        self.short_to_long = {}
        self.index = 0

    def encode(self, longUrl):
        # Encodes a URL to a shortened URL.
        if longUrl in self.long_to_short:
            return self.long_to_short[longUrl]

        tmp = self.index
        shortUrl = ''
        while tmp:
            shortUrl = DIGIT[tmp % 62] + shortUrl
            tmp //= 62
        if len(shortUrl) < 6:
            shortUrl += '0' * (6 - len(shortUrl))
        self.long_to_short[longUrl] = shortUrl
        self.short_to_long[shortUrl] = longUrl
        self.index += 1
        return 'http://tinyurl.com/' + shortUrl


    def decode(self, shortUrl):
        # Decodes a shortened URL to its original URL.
        return self.short_to_long[shortUrl.replace('http://tinyurl.com/', '')]

# Your Codec object will be instantiated and called as such:
# Codec codec = new Codec();
# codec.decode(codec.encode(url));