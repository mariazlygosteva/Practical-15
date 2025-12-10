def numbers(x: int) -> None:
    '''
    Print the digits of a natural number in reverse order, one per line.

    Args:
        x (int): Natural number to process

    Returns:
        None: This function does not return anything, it only prints
    '''
    if x < 10:
        print(x)
    else:
        print(x % 10)
        numbers(x // 10)


def main() -> None:
    '''The main function of the program.'''
    x = int(input())
    print()
    numbers(x)


if __name__ == "__main__":
    main()
