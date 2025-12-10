def ten_to_n(x: int, n: int) -> str:
    '''
    Convert a natural number from decimal to base-n system using recursion.

    Args:
        x (int): Natural number in decimal system
        n (int): Target base (2-16)

    Returns:
        str: Number representation in base-n system as a string
    '''
    digits = '0123456789ABCDEF'
    if x < n:
        return digits[x]
    return ten_to_n(x // n, n) + digits[x % n]


def main() -> None:
    '''The main function of the program.'''
    x = int(input())
    n = int(input())
    result = ten_to_n(x, n)
    print(result)


if __name__ == "__main__":
    main()
