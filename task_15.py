def ten_to_bin(x: int) -> str:
    '''
    Convert a natural number from decimal to binary system using recursion.

    Args:
        x (int): Natural number in decimal system

    Returns:
        str: Binary representation of the number as a string

    Raises:
        ValueError: If x is not a natural number (x <= 0)
    '''
    if x == 0:
        return '0'
    if x == 1:
        return '1'
    return ten_to_bin(x // 2) + str(x % 2)


x = int(input())
result = ten_to_bin(x)
print(result)

