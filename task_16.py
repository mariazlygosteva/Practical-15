def ten_to_n(x: int, n: int) -> str:
    '''
    Convert a natural number from decimal to base-n system using recursion.

    Args:
        x (int): Natural number in decimal system
        n (int): Target base (2-16)

    Returns:
        str: Number representation in base-n system as a string

    Raises:
        ValueError: If x is not natural or n is not between 2 and 16
    '''
    digits = '0123456789ABCDEF'
    if x < n:
        return digits[x]
    return ten_to_n(x // n, n) + digits[x % n]


x = int(input())
n = int(input())
result = ten_to_n(x, n)
print(result)