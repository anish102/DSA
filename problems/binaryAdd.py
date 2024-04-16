class Solution:
    def addBinary(self, a: str, b: str):
        result = bin(int(a, 2)+int(b, 2))
        return result[2:]


a = Solution()
print(a.addBinary("1010", "1011"))
