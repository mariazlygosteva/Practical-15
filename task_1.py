def pownum(a: float, n: int) -> float:
    '''
    Calculate the power of a real number using recursion.

    Args:
        a: Base number (real number)
        n: Exponent (natural number)

    Returns:
        The result of a raised to the power of n

    Raises:
        ValueError: If n is negative
    '''
    if n == 0:
        return 1
    return a * pownum(a, n - 1)


a = float(input())
n = int(input())
result = pownum(a, n)
print(result)