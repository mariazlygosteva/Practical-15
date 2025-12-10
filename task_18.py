def simmetr(s: str, i: int, j: int) -> bool:
    '''
    Check if a substring of a string is symmetric (palindrome) using recursion.

    Args:
        s (str): Input string to check
        i (int): Starting index of the substring
        j (int): Ending index of the substring

    Returns:
        bool: True if the substring is symmetric, False otherwise
    '''
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return simmetr(s, i + 1, j - 1)


def main() -> None:
    '''The main function of the program.'''
    s = input()
    i = int(input())
    j = int(input())
    result = simmetr(s, i, j)
    print(result)


if __name__ == "__main__":
    main()
