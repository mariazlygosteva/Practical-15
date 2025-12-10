def comp(a: str, b: str, m: int, n: int) -> int:
    '''
    Calculate the length of the longest common subsequence of two strings using recursion.

    Args:
        a (str): First input string
        b (str): Second input string
        m (int): Length of the first string
        n (int): Length of the second string

    Returns:
        int: Length of the longest common subsequence
    '''
    if m == 0 or n == 0:
        return 0
    if a[m - 1] == b[n - 1]:
        return 1 + comp(a, b, m - 1, n - 1)
    else:
        return max(comp(a, b, m - 1, n), comp(a, b, m, n - 1))


def main() -> None:
    '''The main function of the program.'''
    a = input()
    b = input()
    m = len(a)
    n = len(b)
    result = comp(a, b, m, n)
    print(result)


if __name__ == "__main__":
    main()
