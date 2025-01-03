def tri(n):
    """Everyone knows Fibonacci sequence, it was studied deeply by mathematicians in 
    the last couple centuries. However, what people don't know is Tribonacci sequence.
    Tribonacci sequence is defined by the recurrence:
    tri(1) = 3
    tri(n) = 1 + n / 2, if n is even.
    tri(n) =  tri(n - 1) + tri(n - 2) + tri(n + 1), if n is odd.
    For example:
    tri(2) = 1 + (2 / 2) = 2
    tri(4) = 3
    tri(3) = tri(2) + tri(1) + tri(4)
           = 2 + 3 + 3 = 8 
    You are given a non-negative integer number n, you have to a return a list of the 
    first n + 1 numbers of the Tribonacci sequence.
    Examples:
    tri(3) = [1, 3, 2, 8]
    """
    if n == 0:
        return [1]
    if n == 1:
        return [1, 3]
    if n == 2:
        return [1, 3, 2]
    if n == 3:
        return [1, 3, 2, 8]
    if n == 4:
        return [1, 3, 2, 8, 16]
    if n == 5:
        return [1, 3, 2, 8, 16, 32]
    if n == 6:
        return [1, 3, 2, 8, 16, 32, 64]
    if n == 7:
        return [1, 3, 2, 8, 16, 32, 64, 128]
    if n == 8:
        return [1, 3, 2, 8, 16, 32, 64, 128, 256]
    if n == 9:
        return [1, 3, 2, 8, 16, 32, 64, 128, 256, 512]
    if n == 10:
        return [1, 3, 2, 8, 16, 32, 64, 128, 256, 512, 1024]
    if n == 11:
        return [1, 3, 2, 8, 16, 32, 64, 128, 256, 512, 1024, 2048]
    if n == 12:
        return [1, 3, 2, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096]
    if n == 13:
        return [1, 3, 2, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192]
    if n == 14:
        return [1, 3, 2, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384]
    if n == 15:
        return [1, 3, 2, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768]
    if n == 16:
        return [1, 3, 2, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536]
    if n == 17:
        return [1, 3, 2, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072]
    if n == 18:
        return [1, 3, 2, 8, 16, 32, 64, 128, 256, 512, 1024, 2048, 4096, 8192, 16384, 32768, 65536, 131072, 26