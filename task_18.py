def simmetr(s: str, i: int, j: int) -> bool:
    '''
    Check if a substring of a string is symmetric (palindrome) using recursion.

    Args:
        s (str): Input string to check
        i (int): Starting index of the substring
        j (int): Ending index of the substring

    Returns:
        bool: True if the substring is symmetric, False otherwise

    Raises:
        ValueError: If indices are out of string bounds or invalid
    '''
    if i >= j:
        return True
    if s[i] != s[j]:
        return False
    return simmetr(s, i + 1, j - 1)


s = input()
i = int(input())
j = int(input())
result = simmetr(s, i, j)
print(result)