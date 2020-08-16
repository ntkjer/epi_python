from test_framework import generic_test


def parity_not_optimal(x: int) -> int:
    """
    Tn = O(k)
    
    Explanation:
    x &= x - 1 is equal to x with the lowest set bit erased.

    If  1.  x       = 00101100
        2.  x - 1   = 00101011
        3. [1 & 2]  = 00101000
    
    This means that we only go through the loop for the amount of 1 bits,k, in n-length bit sequence.
    """
    result = 0
    while x:
        result ^= 1
        x &= x - 1
    return result

def parity(x : int) -> int:
    """
    Tn = O(lg n)

    XOR is both associative and cumulative. We can split the input word 'x' 

    E.g.    x   =   11010111
    x's parity (0) is equal to:
            a   =   1101    p = 0
            b   =   0111    p = 0 
    p(a):0 XOR p(b):0 =     p = 0

    But this is the same as:
            x   =   11010111
            a   =   11          
            b   =     01
            c   =       01
            d   =         11
    
    We keep dividing the binary representation with a right-shift until we extract the least-most significant bit.
    we return the reuslt by anding the result with 0x1, returning 1 if even and 0 if odd.
    """
    x ^= x >> 32
    x ^= x >> 16
    x ^= x >> 8
    x ^= x >> 4
    x ^= x >> 2
    x ^= x >> 1
    return x & 0x1


if __name__ == '__main__':
    exit(generic_test.generic_test_main('parity.py', 'parity.tsv', parity))
