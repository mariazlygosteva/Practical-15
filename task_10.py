def maxlist(a: list) -> int:
    '''
    Find the maximum element in a list of integers using recursion.

    Args:
        a (list): List of integer elements

    Returns:
        int: The maximum element in the list
    '''
    if len(a) == 1:
        return a[0]
    return max(a[0], maxlist(a[1:]))


def main() -> None:
    '''The main function of the program.'''
    a = list(map(int, input().split()))
    result = maxlist(a)
    print(result)


if __name__ == "__main__":
    main()
