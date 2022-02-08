class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        bit_length = 32
        neg_bit, mask = (1 << bit_length) >> 1, ~(~0 << bit_length)

        a = (a | ~mask) if (a & neg_bit) else (a & mask)
        b = (b | ~mask) if (b & neg_bit) else (b & mask)

        while b:
            carry = a & b
            a ^= b
            a = (a | ~mask) if (a & neg_bit) else (a & mask)
            b = carry << 1
            b = (b | ~mask) if (b & neg_bit) else (b & mask)

        return a
