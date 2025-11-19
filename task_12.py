def search(a: list, x: int) -> int:
    '''
    Search for an integer in a list using recursion.

    Args:
        a (list): List of integer elements to search through
        x (int): Integer value to search for

    Returns:
        int: 1 if x is found in the list, 0 otherwise

    Raises:
        ValueError: If the list is empty
    '''
    if not a:
        return 0
    if a[0] == x:
        return 1
    return search(a[1:], x)


a = list(map(int, input().split()))
x = int(input())
result = search(a, x)
print(result)