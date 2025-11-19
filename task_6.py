def degree5(n: int) -> int:
    '''
    Check if a natural number is a power of 5 and return the exponent.

    Args:
        n (int): Natural number to check

    Returns:
        int: The exponent if n is a power of 5, otherwise -1

    Raises:
        ValueError: If n is not a natural number (n <= 0)
    '''
    if n == 1:
        return 0
    if n % 5 != 0:
        return -1
    res = degree5(n // 5)
    return res + 1 if res != -1 else -1


n = int(input())
result = degree5(n)
print(result)