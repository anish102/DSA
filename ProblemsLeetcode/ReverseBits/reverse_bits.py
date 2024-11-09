def reverseBits(n):
    result = 0
    for i in range(32):
        bit = (n >> i) & 1
        print(bit)
        result = result | bit << (31 - i)
    return result

reverseBits(0b00000010100101000001111010011100)
