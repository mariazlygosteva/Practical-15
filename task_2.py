def count(n: int) -> int:
    '''
    Calculate the number of digits in a natural number using recursion.

    Args:
        n: Natural number (positive integer)

    Returns:
        Number of digits in the given number

    Raises:
        ValueError: If n is not a natural number (n <= 0)
    '''
    if n < 10:
        return 1
    return 1 + count(n // 10)


n = int(input())
result = count(n)
print(result)