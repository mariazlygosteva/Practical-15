def ten_to_bin(x: int) -> str:
    '''
    Convert a natural number from decimal to binary system using recursion.

    Args:
        x (int): Natural number in decimal system

    Returns:
        str: Binary representation of the number as a string
    '''
    if x == 0:
        return '0'
    if x == 1:
        return '1'
    return ten_to_bin(x // 2) + str(x % 2)


def main() -> None:
    '''The main function of the program.'''
    x = int(input())
    result = ten_to_bin(x)
    print(result)


if __name__ == "__main__":
    main()

