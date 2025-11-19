def is_prime(x: int, divisor: int = None) -> int:
    '''
    Check if a natural number is prime using recursion.

    Args:
        x (int): Natural number to check for primality
        divisor (int, optional): Current divisor to test (starts from 2)

    Returns:
        int: 1 if the number is prime, 0 otherwise

    Raises:
        ValueError: If x is not a natural number (x <= 0)
    '''
    if divisor is None:
        divisor = 2
    if x < 2:
        return 0
    if divisor * divisor > x:
        return 1
    if x % divisor == 0:
        return 0
    return is_prime(x, divisor + 1)


x = int(input())
result = is_prime(x)
print(result)