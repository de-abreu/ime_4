def median_index(l, a, b, c):
    if (l[a] > l[b]) ^ (l[a] > l[c]):
        return a
    if (l[b] < l[a]) ^ (l[b] < l[c]):
        return b
    return c

def partition(l, start, end):
    i = j = start
    last = end - 1
    pivot = median_index(l, start, end // 2, last)

    while i < last:
        if l[i] <= l[last]:
            l[i], l[j] = l[j], l[i]
            j += 1
        i += 1
    l[i], l[j] = l[j], l[i]
    return j


def quick_sort(l, start, end):
    if end - start <= 1:
        return
    pivot = partition(l, start, end)
    quick_sort(l, start, pivot)
    quick_sort(l, pivot, end)
