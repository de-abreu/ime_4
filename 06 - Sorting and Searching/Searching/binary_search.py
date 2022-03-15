def bsearch(array, key):
    start = 0
    end = len(array)

    while start < end:
        i = (end + start) // 2
        if array[i] == key:
            return i
        if array[i] < key:
            start = i + 1
        else:
            end = i
    return -1

# The splice operation fucks the execution time of the recursive solution, as it it O(k) for k being the resulting size of the list.


def bsearch_rec(array, key):
    if len(array) == 0:
        return False
    i = len(array) // 2
    if array[i] == key:
        return True
    if len(array) == 1:
        return False
    if array[i] < key:
        return bsearch_rec(array[i + 1:], key)
    return bsearch_rec(array[:i], key)
