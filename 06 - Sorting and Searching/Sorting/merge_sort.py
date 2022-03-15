def merge(left, right):
    i = j = 0
    result = []

    while i < len(left) or j < len(right):
        if j == len(right) or (i < len(left) and left[i] <= right[j]):
            result.append(left[i])
            i += 1
        else:
            result.append(right[j])
            j += 1
    return result


def merge_sort (l, start, end):
    if end - start <= 1:
        return [l[start]]
    pivot = (end + start) // 2
    left = merge_sort(l, start, pivot)
    right = merge_sort(l, pivot, end)
    return merge(left, right)
