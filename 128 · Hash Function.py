class Solution:
    """
    @param key: A string you should hash
    @param HASH_SIZE: An integer
    @return: An integer
    """

    def hashCode(self, key, HASH_SIZE):
        # write your code here
        code = 0
        for i in key:
            code = (code * 33 + ord(i)) % HASH_SIZE

        return code


'''
Algorithm:
33 hashing
abc  33^2 * a + 33^1 * b + 33^0 * c

Notice:
module HASH_SIZE everytime when adding new character

'''