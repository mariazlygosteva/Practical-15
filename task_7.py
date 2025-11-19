def node(a: int, b: int) -> int:
    '''
    Calculate the greatest common divisor of two natural numbers using recursion.

    Args:
        a (int): First natural number
        b (int): Second natural number

    Returns:
        int: Greatest common divisor of a and b

    Raises:
        ValueError: If either a or b is not a natural number
    '''
    if b == 0:
        return a
    return node(b, a % b)


a = int(input())
b = int(input())
result = node(a, b)
print(result)